const API_URL = "http://127.0.0.1:8000";

async function parseResponse(response) {
  if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`);
  }

  return response.json();
}

export async function askQuestion(
  question,
  chatId
) {
  const response = await fetch(
    `${API_URL}/ask`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        question,
        chat_id: chatId,
      }),
    }
  );

  return parseResponse(response);
}

export async function createNewChat() {
  const response = await fetch(
    `${API_URL}/new-chat`,
    {
      method: "POST",
    }
  );

  return parseResponse(response);
}

export async function uploadFile(file) {
  const formData = new FormData();

  formData.append(
    "file",
    file
  );

  const response = await fetch(
    `${API_URL}/upload`,
    {
      method: "POST",
      body: formData,
    }
  );

  return parseResponse(response);
}

export async function getDocuments() {
  const response = await fetch(
    `${API_URL}/documents`
  );

  return parseResponse(response);
}

export async function getMetrics() {
  const response = await fetch(
    `${API_URL}/metrics`
  );

  return parseResponse(response);
}

export async function getHistory() {
  const response = await fetch(
    `${API_URL}/history`
  );

  return parseResponse(response);
}

export async function deleteChat(chatId) {

  const response = await fetch(
    `${API_URL}/history/${chatId}`,
    {
      method: "DELETE",
    }
  );

  return parseResponse(response);
}

export async function getEvaluation() {

  const response = await fetch(
    `${API_URL}/evaluate`
  );

  return parseResponse(response);
}

/* ---------------- DOWNLOAD PDF ---------------- */

export async function downloadPDF(
  question,
  answer
) {
  const response = await fetch(
    `${API_URL}/export/pdf`,
    {
      method: "POST",
      headers: {
        "Content-Type":
          "application/json",
      },
      body: JSON.stringify({
        question,
        answer,
      }),
    }
  );

  const blob =
    await response.blob();

  const url =
    window.URL.createObjectURL(
      blob
    );

  const a =
    document.createElement(
      "a"
    );

  a.href = url;
  a.download = "answer.pdf";

  document.body.appendChild(a);

  a.click();

  a.remove();

  window.URL.revokeObjectURL(
    url
  );
}

/* ---------------- DOWNLOAD DOCX ---------------- */

export async function downloadDOCX(
  question,
  answer
) {
  const response = await fetch(
    `${API_URL}/export/docx`,
    {
      method: "POST",
      headers: {
        "Content-Type":
          "application/json",
      },
      body: JSON.stringify({
        question,
        answer,
      }),
    }
  );

  const blob =
    await response.blob();

  const url =
    window.URL.createObjectURL(
      blob
    );

  const a =
    document.createElement(
      "a"
    );

  a.href = url;
  a.download = "answer.docx";

  document.body.appendChild(a);

  a.click();

  a.remove();

  window.URL.revokeObjectURL(
    url
  );
}

/* ---------------- DOWNLOAD EXCEL ---------------- */

export async function downloadExcel(
  question,
  answer
) {
  const response = await fetch(
    `${API_URL}/export/excel`,
    {
      method: "POST",
      headers: {
        "Content-Type":
          "application/json",
      },
      body: JSON.stringify({
        question,
        answer,
      }),
    }
  );

  const blob =
    await response.blob();

  const url =
    window.URL.createObjectURL(
      blob
    );

  const a =
    document.createElement(
      "a"
    );

  a.href = url;
  a.download = "answer.xlsx";

  document.body.appendChild(a);

  a.click();

  a.remove();

  window.URL.revokeObjectURL(
    url
  );
}
