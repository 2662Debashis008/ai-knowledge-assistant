export default function CitationBox({
  citations,
}) {
  if (!citations?.length) {
    return null;
  }

  return (
    <section className="mt-5">

      <h3 className="section-label">
        Citations
      </h3>

      <ul className="mt-3 grid gap-2">

        {citations.map(
          (item, index) => (
            <li
              className="citation-item"
              key={`${item.source}-${index}`}
            >
              <span className="citation-index">
                {index + 1}
              </span>
              <span className="min-w-0 truncate">
                {item.source}
              </span>
            </li>
          )
        )}

      </ul>

    </section>
  );
}
