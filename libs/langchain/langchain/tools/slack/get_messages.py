import json
import logging
from typing import Dict, Optional

from langchain.callbacks.manager import CallbackManagerForToolRun
from langchain.tools.slack.base import SlackBaseTool


class SlackGetMessagesSchema(BaseModel):
    """Input schema for SlackGetMessages."""
    channel_id: str = Field(
        ...,
        description="The channel id, private group, or IM channel to send message to.",
    )

class SlackGetMessages(SlackBaseTool):
    name: str = "get_messages"
    description: str = "Use this tool to get channel messages history."
    args_schema: Type[SlackGetMessagesSchema] = SlackGetMessagesSchema

    def _run(
        self,
        channel_id: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        logging.getLogger(__name__)

        result = self.client.conversations_history(channel_id)
        conversation_history = []
        conversation_history = result["messages"]

        output_json = json.dumps(conversation_history)

        return output_json
