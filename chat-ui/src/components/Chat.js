'use client'

import { useState } from "react";
import axios from "axios";

export default function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMessage = { role: "user", content: input };
    const updatedMessages = [...messages, userMessage];
    setInput("")
    setMessages(updatedMessages);

    try {
      const res = await axios.post("http://127.0.0.1:8000/api/chat/", { messages: updatedMessages });
      const botMessage = { role: "assistant", content: res.data.reply };
      setMessages([...updatedMessages, botMessage]);
    } catch (error) {
      console.error("Error sending message:", error);
    }

    setInput("");
  };

  return (
    <div className="max-w-2xl mx-auto p-4 bg-gray-100 rounded-lg shadow-lg h-screen flex flex-col">
      <div className="flex-1 overflow-y-auto p-2">
        {messages.map((msg, index) => (
          <div key={index} className={`my-2 p-2 rounded-lg ${msg.role === "user" ? "bg-blue-500 text-white self-end" : "bg-gray-300 text-black self-start"}`}>
            {msg.content}
          </div>
        ))}
      </div>
      <div className="flex">
        <input
          className="flex-1 p-2 border rounded-lg text-black placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === "Enter" && sendMessage()}
        />
        <button className="ml-2 p-2 bg-blue-500 text-white rounded-lg" onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  );
}
