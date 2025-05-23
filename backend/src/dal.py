# dal.py will handle mongo db interactions
# Standard inbuilt libraries
from uuid import uuid4
# Third-party libraries
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ReturnDocument
from pydantic import BaseModel

class ListSummary(BaseModel):
    """
    Create ListSummary instances from MongoDB documents
    """
    id: str
    name: str
    item_count: int

    @staticmethod
    def from_doc(doc) -> "ListSummary":
        return ListSummary(
            id=str(doc["_id"]),
            name=doc["name"],
            item_count=doc["item_count"]
            )

# Data Models
class ToDoListItem(BaseModel):
    """
    Create ToDoListItem instances from MongoDB documents
    """
    id: str
    label: str
    checked: bool
    
    @staticmethod
    def from_doc(item) -> "ToDoListItem":
        return ToDoListItem(
            id=item["id"],
            label=item["label"],
            checked=item["checked"]
            )


class ToDoList(BaseModel):
    """
    Create ToDoList instances from MongoDB documents
    """
    id: str
    name: str
    items: list[ToDoListItem]
    
    @staticmethod
    def from_doc(doc) -> "ToDoList":
        return ToDoList(
            id=str(doc["_id"]),
            name=doc["name"],
            items=[ToDoListItem.from_doc(item) for item in doc["items"]]    
            )


class ToDoDAL:
    """
    Will encapsulate all MongoDB operations.
    """
    def _init_(self, todo_collection: AsyncIOMotorClient):
        self._todo_collection = todo_collection

    async def list_todo_lists(self, session=None):
        async for doc in self._todo_collection.find(
            {}, 
            projection={"name": 1, "item_count": {"$size": "$items"}},
            sort={"name": 1},
            session=session
        ):
            yield ListSummary.from_doc(doc)

    async def create_todo_list(self, name: str, session=None) -> str:
        response = await self._todo_collection.insert_one(
            {"name": name, "items":[]}, 
            session=session
        )
        return str(response.inserted_id)

    async def get_todo_list(self, id: str | ObjectId, session=None) -> ToDoList:
        doc = await self._todo_collection.find_one(
            {"_id": ObjectId(id)},
            session=session,
        )
        return ToDoList.from_doc(doc)

    async def delete_todo_list(self, id: str | ObjectId, session=None) -> bool:
        response = await self._todo_collection.delete_one(
            {"_id": ObjectId(id)},
            session=session
        )
        return response.deleted_count == 1

    async def create_item( self, id: str | ObjectId, label: str, session=None) -> ToDoList | None:
        result = await self._todo_collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {
                "$push": {
                "items": {
                    "id": uuid4().hex,
                    "label": label,
                    "checked": False
                    }
                }
            },
            session=session,
            return_document = ReturnDocument.AFTER
        )
        if result:
            return ToDoList.from_doc(result)

    async def set_checked_state(self, doc_id: str | ObjectId, item_id: str, checked_state: bool, session=None) -> ToDoList | None:
        result = await self._todo_collection.find_one_and_update(
            {"_id": ObjectId(doc_id), "items.id": item_id},
            {"$set": {"items.$.checked": checked_state}},
            session=session,
            return_document=ReturnDocument.AFTER
        )
        if result:
            return ToDoList.from_doc(result)

    async def delete_item(self, doc_id: str | ObjectId, item_id: str, session=None) -> ToDoList | None:
        result = await self._todo_collection.find_one_and_update(
            {"_id": ObjectId(doc_id)}, 
            {"$pull": {"items": {"id": item_id}}},
            session=session,
            return_document=ReturnDocument.AFTER
        )
        if result:
            return ToDoList.from_doc(result)