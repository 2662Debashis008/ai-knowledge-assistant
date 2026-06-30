"use client";

import { useState } from "react";
import { uploadFile } from "../services/api";

export default function UploadBox({
  onUploaded,
}) {
  const [file, setFile] =
    useState(null);

  const [message, setMessage] =
    useState("");

  const [uploading, setUploading] =
    useState(false);

  async function handleUpload() {
    if (!file) return;

    setUploading(true);
    setMessage("");

    try {
      const result =
        await uploadFile(file);

      setMessage(
        result.error ||
        result.message ||
        "Upload complete"
      );

      if (!result.error) {
        onUploaded?.();
      }
    } catch (error) {
      console.error(error);
      setMessage(
        "Upload failed. Check the backend server."
      );
    } finally {
      setUploading(false);
    }
  }

  return (
    <section className="panel">

      <div className="panel-heading">
        <div>
          <p className="eyebrow">
            Ingestion
          </p>
          <h2>
            Upload document
          </h2>
        </div>
      </div>

      <label className="file-drop">
        <input
          type="file"
          onChange={(e) =>
            setFile(e.target.files[0])
          }
        />
        <span className="file-icon">
          +
        </span>
        <span className="file-name">
          {file ? file.name : "Choose PDF, DOCX, CSV, MD"}
        </span>
      </label>

      <button
        className="primary-button mt-4 w-full"
        disabled={!file || uploading}
        onClick={handleUpload}
      >
        {uploading ? "Indexing..." : "Upload and index"}
      </button>

      {message && (
        <p className="status-text">
          {message}
        </p>
      )}

    </section>
  );
}
