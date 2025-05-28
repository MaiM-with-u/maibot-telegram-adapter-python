from telegram.ext.filters import ChatType
from telegram import Message
from src.config import global_config


def global_ban_filter(message: Message) -> bool:
    if global_config.ban_user_id is None:
        return True
    return message.from_user.id not in global_config.ban_user_id


def list_filter(message: Message, list_type: str, chat_list: list[int]) -> bool:
    if not global_ban_filter(message):
        return False
    if list_type == "whitelist":
        return message.chat.id in chat_list
    elif list_type == "blacklist":
        return message.chat.id not in chat_list
    else:
        return False


class GroupsFilter(ChatType._Groups):
    def filter(self, message: Message) -> bool:
        is_groups = super().filter(message)
        in_list = list_filter(
            message=message, list_type=global_config.group_list_type, chat_list=global_config.group_list
        )
        return is_groups and in_list


class PrivateFilter(ChatType._Private):
    def filter(self, message: Message) -> bool:
        is_private = super().filter(message)
        in_list = list_filter(
            message=message, list_type=global_config.private_list_type, chat_list=global_config.private_list
        )
        return is_private and in_list


groups_filter = GroupsFilter(name="custom_groups_filter")
private_filter = PrivateFilter(name="custom_private_filter")
