"use client";

import { useState } from "react";

import ChatBox from "../components/ChatBox";
import DocumentList from "../components/DocumentList";
import HistoryPanel from "../components/HistoryPanel";
import EvaluationPanel from "../components/EvaluationPanel";
export default function Home() {
  const [refreshKey, setRefreshKey] = useState(0);
  const [theme, setTheme] = useState("dark");
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [chatResetKey, setChatResetKey] = useState(0);
  const [selectedChat, setSelectedChat] = useState(null);

  function refreshData() {
    setRefreshKey((key) => key + 1);
  }

  function startNewChat() {
    setSelectedChat(null);
    setChatResetKey((key) => key + 1);
  }

  function toggleTheme() {
    setTheme((currentTheme) =>
      currentTheme === "dark" ? "light" : "dark"
    );
  }

  const isDark = theme === "dark";

  return (
    <main className={`app-shell ${isDark ? "theme-dark" : "theme-light"} ${sidebarOpen ? "sidebar-open" : "sidebar-closed"}`}>
      <header className="topbar">
        <div className="topbar-brand">
          <button
            aria-label="Toggle sidebar"
            className="hamburger-button"
            onClick={() => setSidebarOpen((open) => !open)}
            type="button"
          >
            <span />
            <span />
            <span />
          </button>
          <div className="chatbot-logo" aria-hidden="true">
            <svg viewBox="0 0 32 32">
              <rect x="6" y="9" width="20" height="16" rx="6" />
              <path d="M12 9V6" />
              <path d="M20 9V6" />
              <circle cx="13" cy="17" r="1.8" />
              <circle cx="19" cy="17" r="1.8" />
              <path d="M13 22h6" />
            </svg>
          </div>
          <h1>AI Assistant</h1>
        </div>

        <div className="navbar-actions">
          <a
            className="source-button"
            href="https://github.com/2662Debashis008/ai-knowledge-assistant"
            target="_blank"
            rel="noopener noreferrer"
          >
            <svg
              aria-hidden="true"
              viewBox="0 0 24 24"
            >
              <path d="M12 2a10 10 0 0 0-3.16 19.49c.5.09.68-.22.68-.48v-1.7c-2.78.6-3.37-1.2-3.37-1.2-.45-1.15-1.11-1.46-1.11-1.46-.91-.62.07-.61.07-.61 1 .07 1.53 1.03 1.53 1.03.9 1.53 2.35 1.09 2.92.83.09-.65.35-1.09.63-1.34-2.22-.25-4.55-1.11-4.55-4.95 0-1.09.39-1.99 1.03-2.69-.1-.25-.45-1.27.1-2.65 0 0 .84-.27 2.75 1.03A9.4 9.4 0 0 1 12 6.96c.85 0 1.7.11 2.5.34 1.9-1.3 2.74-1.03 2.74-1.03.55 1.38.2 2.4.1 2.65.64.7 1.03 1.6 1.03 2.69 0 3.85-2.34 4.69-4.57 4.94.36.31.68.92.68 1.86v2.6c0 .26.18.58.69.48A10 10 0 0 0 12 2Z" />
            </svg>
            Source Code
          </a>

          <button
            aria-label={isDark ? "Switch to light theme" : "Switch to dark theme"}
            className="theme-icon-button"
            onClick={toggleTheme}
            type="button"
          >
            {isDark ? (
              <svg
                aria-hidden="true"
                key="sun"
                viewBox="0 0 24 24"
              >
                <circle cx="12" cy="12" r="4" />
                <path d="M12 2v2" />
                <path d="M12 20v2" />
                <path d="M4.93 4.93l1.41 1.41" />
                <path d="M17.66 17.66l1.41 1.41" />
                <path d="M2 12h2" />
                <path d="M20 12h2" />
                <path d="M4.93 19.07l1.41-1.41" />
                <path d="M17.66 6.34l1.41-1.41" />
              </svg>
            ) : (
              <svg
                aria-hidden="true"
                key="moon"
                viewBox="0 0 24 24"
              >
                <path d="M21 14.5A8.5 8.5 0 0 1 9.5 3a7 7 0 1 0 11.5 11.5Z" />
              </svg>
            )}
          </button>
        </div>
      </header>

      <div className="convo-layout">
        <aside className="options-sidebar">
          <button
            className="new-chat-button"
            onClick={startNewChat}
            type="button"
          >
            + New Chat
          </button>

          <HistoryPanel
            refreshKey={refreshKey}
            onSelectChat={(chat) => {
              setSelectedChat(chat);
              setChatResetKey((key) => key + 1);
            }}
          />
          <DocumentList
            refreshKey={refreshKey}
            onDeleted={refreshData}
          />
        </aside>
        
        <ChatBox
          key={chatResetKey}
          selectedChat={selectedChat}
          onAnswered={refreshData}
          onUploaded={refreshData}
        />
      </div>
    </main>
  );
}
