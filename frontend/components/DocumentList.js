"use client";

import {
  useEffect,
  useState,
} from "react";

import {
  getMetrics,
  getDocuments,
} from "../services/api";

export default function DocumentList({
  refreshKey = 0,
}) {

  const [docs, setDocs] =
    useState([]);

  const [metrics, setMetrics] =
    useState({ documents: 0 });

  const [loading, setLoading] =
    useState(true);

  const [expanded, setExpanded] =
    useState(false);

  useEffect(() => {

    async function load() {

      setLoading(true);

      try {

        const [
          documentResult,
          metricResult,
        ] = await Promise.all([
          getDocuments(),
          getMetrics(),
        ]);

        setDocs(
          documentResult.documents || []
        );

        setMetrics(
          metricResult || {
            documents: 0,
          }
        );

      } catch (error) {

        console.error(error);

      } finally {

        setLoading(false);

      }
    }

    load();

  }, [refreshKey]);

  return (
    <section className="panel sidebar-section">

      <div className="panel-heading">
        <h2>
          Documents (
          {metrics.documents ??
            docs.length}
          )
        </h2>
      </div>

      <button
        className="show-documents-button"
        onClick={() =>
          setExpanded(
            (open) => !open
          )
        }
        type="button"
      >
        {expanded
          ? "Hide Documents"
          : "Show Documents"}

        <span>
          {expanded ? "^" : "v"}
        </span>
      </button>

      {expanded && (

        loading ? (

          <div className="skeleton-list">
            <span />
            <span />
            <span />
          </div>

        ) : (

          <ul className="document-list">

            {docs.length === 0 && (
              <li className="empty-state">
                No documents indexed.
              </li>
            )}

            {docs.map(
              (doc, index) => (
                <li
                  className="document-item"
                  key={`${doc}-${index}`}
                  title={doc}
                >
                  <span className="document-glyph" />

                  <span className="truncate">
                    {doc}
                  </span>
                </li>
              )
            )}

          </ul>

        )
      )}

    </section>
  );
}