from django.shortcuts import render

# Create your views here.
from openai import OpenAI

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Conversation
from .serializers import ConversationSerializer
from django.conf import settings

# Set Key as env_var before running code
client = OpenAI()

@api_view(['POST'])
def chat(request):
    messages = request.data.get('messages', '')

    conversation_history = [
    {"role": "system", "content": f"You are a highly sarcastic and witty AI. Respond to the following statement with a humorous and sarcastic remark"}
    ]

    # Not safe. Need to fix.

    conversation_history.extend(messages)
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages= conversation_history,
    temperature=0.7,
    )
    conversation_history.append({"role": "assistant", "content": response.choices[0].message.content})

    bot_reply = response.choices[0].message.content

    # Save conversation to DB
    # conversation = Conversation.objects.create(user_message=user_message, bot_response=bot_reply)

    return Response({"reply": bot_reply})
