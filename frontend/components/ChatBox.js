"use client";

import { useState } from "react";

import {
  askQuestion,
  createNewChat,
  downloadDOCX,
  downloadExcel,
  downloadPDF,
  uploadFile,
} from "../services/api";

import CitationBox from "./CitationBox";
import LoadingSpinner from "./LoadingSpinner";

export default function ChatBox({
  selectedChat,
  onAnswered,
  onUploaded,
}) {
  const [question, setQuestion] = useState("");
  const [pendingQuestion, setPendingQuestion] = useState("");
  const [turns, setTurns] = useState(
    selectedChat?.messages || []
  );
  const [uploadMessage, setUploadMessage] = useState("");

  const [loading, setLoading] = useState(false);
  const [uploading, setUploading] = useState(false);
  const [chatId, setChatId] = useState(
    selectedChat?.chat_id || null
  );

  async function handleAsk() {
  const trimmedQuestion = question.trim();

  if (!trimmedQuestion || loading) return;

  setLoading(true);
  setPendingQuestion(trimmedQuestion);
  setQuestion("");

  try {

    let currentChatId =
      chatId || selectedChat?.chat_id;

    if (!currentChatId) {

      const chat = await createNewChat();

      currentChatId = chat.chat_id;

      setChatId(currentChatId);
    }

    const result = await askQuestion(
      trimmedQuestion,
      currentChatId
    );

    setTurns((currentTurns) => [
      ...currentTurns,
      {
        question: trimmedQuestion,
        answer: result.answer,
        citations: result.citations || [],
      },
    ]);

    onAnswered?.();

  } catch (error) {

    console.error(error);

    setTurns((currentTurns) => [
      ...currentTurns,
      {
        question: trimmedQuestion,
        answer: "Failed to get response from server.",
        citations: [],
      },
    ]);

  } finally {

    setLoading(false);
    setPendingQuestion("");
  }
}

  async function handleFileUpload(file) {
    if (!file || uploading) return;

    setUploading(true);
    setUploadMessage(`Uploading ${file.name}...`);

    try {
      const result = await uploadFile(file);

      setUploadMessage(
        result.error ||
          `${result.file || file.name} indexed successfully.`
      );

      if (!result.error) {
        onUploaded?.();
      }
    } catch (error) {
      console.error(error);

      setUploadMessage(
        "Upload failed. Check the backend server."
      );
    } finally {
      setUploading(false);
    }
  }

  return (
    <section className="workspace-panel">
      <p className="chat-status">
        Welcome to AI Assistant
      </p>

      <div className="message-stream">
        {turns.length === 0 && !loading && (
          <div className="welcome-card">
            <h2>
              Upload documents and ask questions.
            </h2>

            <p>
              Attach PDF, DOCX, CSV, or Markdown files
              with the plus button, then ask anything
              from your indexed knowledge base.
            </p>
          </div>
        )}

        {turns.map((turn, index) => (
          <div key={`${turn.question}-${index}`}>
            <div className="chat-turn user-turn">
              <p className="turn-label">
                User:
              </p>

              <p>{turn.question}</p>
            </div>

            <div className="chat-turn assistant-turn">
              <div className="answer-header">
                <p className="turn-label">
                  Assistant:
                </p>

                <div className="export-actions">
                  <button
                    onClick={() =>
                      downloadPDF(turn.question, turn.answer)
                    }
                  >
                    PDF
                  </button>

                  <button
                    onClick={() =>
                      downloadDOCX(turn.question, turn.answer)
                    }
                  >
                    DOCX
                  </button>

                  <button
                    onClick={() =>
                      downloadExcel(turn.question, turn.answer)
                    }
                  >
                    XLSX
                  </button>
                </div>
              </div>

              <p className="answer-text">
                {turn.answer}
              </p>

              <CitationBox
                citations={turn.citations || []}
              />
            </div>
          </div>
        ))}

        {loading && (
          <>
            <div className="chat-turn user-turn">
              <p className="turn-label">
                User:
              </p>

              <p>{pendingQuestion}</p>
            </div>

            <div className="chat-turn assistant-turn">
              <p className="turn-label">
                Assistant:
              </p>

              <LoadingSpinner />
            </div>
          </>
        )}
      </div>

      {uploadMessage && (
        <p className="composer-status">
          {uploadMessage}
        </p>
      )}

      <div className="question-box">
        <input
          className="hidden-file-input"
          disabled={uploading}
          id="composer-file-upload"
          type="file"
          onChange={(event) => {
            const file =
              event.target.files?.[0];

            handleFileUpload(file);

            event.target.value = "";
          }}
        />

        <label
          htmlFor="composer-file-upload"
          className="attach-button"
          title="Upload document"
        >
          +
        </label>

        <input
          type="text"
          placeholder="Type your message here"
          value={question}
          onChange={(e) => {
            setQuestion(e.target.value);
          }}
          onKeyDown={(event) => {
            if (event.key === "Enter") {
              handleAsk();
            }
          }}
        />

        <button
          className="primary-button"
          disabled={
            !question.trim() || loading
          }
          onClick={handleAsk}
        >
          {loading ? "Wait" : "Submit"}
        </button>
      </div>
    </section>
  );
}
