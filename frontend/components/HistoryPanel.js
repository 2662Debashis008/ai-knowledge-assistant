"use client";

import { useEffect, useState } from "react";

import {
  getHistory,
  deleteChat,
} from "../services/api";

export default function HistoryPanel({
  refreshKey = 0,
  onSelectChat,
}) {

  const [history, setHistory] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  useEffect(() => {

    let isMounted = true;

    async function loadHistory() {

      try {

        const result =
          await getHistory();

        if (!isMounted) {
          return;
        }

        setHistory(
          Array.isArray(result)
            ? [...result].reverse()
            : []
        );

      } catch (error) {

        console.error(error);

        if (isMounted) {
          setHistory([]);
        }

      } finally {

        if (isMounted) {
          setLoading(false);
        }

      }
    }

    loadHistory();

    return () => {
      isMounted = false;
    };

  }, [refreshKey]);

  async function handleDelete(
    e,
    chatId
  ) {

    e.stopPropagation();

    try {

      await deleteChat(chatId);

      setHistory((current) =>
        current.filter(
          (chat) =>
            chat.chat_id !== chatId
        )
      );

    } catch (error) {

      console.error(
        "Delete failed",
        error
      );

    }
  }

  return (
    <section className="panel sidebar-section">

      <div className="panel-heading">
        <h2>
          Recent Chats
        </h2>
      </div>

      {loading ? (

        <div className="skeleton-list">
          <span />
          <span />
        </div>

      ) : (

        <div className="history-list">

          {history.length === 0 && (
            <div className="empty-state">
              No chats yet
            </div>
          )}

          {history.map((item) => (

            <div
              key={item.chat_id}
              className="history-row"
            >

              <button
                className="history-item"
                onClick={() =>
                  onSelectChat?.(item)
                }
                type="button"
              >
                <p>
                  {item.title ||
                    item.messages?.[0]?.question ||
                    "Untitled chat"}
                </p>
              </button>

              <button
  className="delete-chat-btn"
  onClick={(e) =>
    handleDelete(e, item.chat_id)
  }
  title="Delete Chat"
  type="button"
>
  <svg
    viewBox="0 0 24 24"
    width="18"
    height="18"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
  >
    <path d="M3 6h18" />
    <path d="M8 6V4h8v2" />
    <path d="M19 6l-1 14H6L5 6" />
    <path d="M10 11v5" />
    <path d="M14 11v5" />
  </svg>
</button>

            </div>

          ))}

        </div>

      )}

    </section>
  );
}
