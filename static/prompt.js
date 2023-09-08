const promptForm = document.getElementById("prompt-form");
const submitButton = document.getElementById("submit-button");
const questionButton = document.getElementById("question-button");
const messagesContainer = document.getElementById("messages-container");
const darkModeButton = document.getElementById("darkModeButton");
const questionsimple = document.getElementById("question-simple-button");
const textButton = document.getElementById("textButton");
const body = document.body;

const appendHumanMessage = (message) => {
  const humanMessageElement = document.createElement("div");
  humanMessageElement.classList.add("message", "message-human");
  humanMessageElement.innerHTML = message;
  messagesContainer.appendChild(humanMessageElement);
};

const appendAIMessage = async (messagePromise) => {
  // Add a loader to the interface
  const loaderElement = document.createElement("div");
  loaderElement.classList.add("message");
  loaderElement.innerHTML =
    "<div class='loader'><div></div><div></div><div></div>";
  messagesContainer.appendChild(loaderElement);

  // Await the answer from the server
  const messageToAppend = await messagePromise();

  // Replace the loader with the answer
  loaderElement.classList.remove("loader");
  loaderElement.innerHTML = messageToAppend;
};

const handlePrompt = async (event) => {
  event.preventDefault();
  // Parse form data in a structured object
  const data = new FormData(event.target);
  promptForm.reset();

  let url = "/prompt";
  if (questionButton.dataset.question !== undefined) {
    url = "/answer";
    data.append("question", questionButton.dataset.question);
    delete questionButton.dataset.question;
    questionButton.classList.remove("hidden");
    questionsimple.classList.remove("hidden");
    submitButton.innerHTML = "Message";
  }
  if (questionsimple.dataset.question !== undefined) {
    url = "/answer";
    data.append("question", questionsimple.dataset.question);
    delete questionsimple.dataset.question;
    questionsimple.classList.remove("hidden");
    questionButton.classList.remove("hidden");
    submitButton.innerHTML = "Message";
  }
  prompt = data.get("prompt")
  appendHumanMessage(prompt);

  await appendAIMessage(async () => {
    const response = await fetch(url, {
      method: "POST",
      body: data,
    });
    const result = await response.json();
    return result.answer;
  });
};

promptForm.addEventListener("submit", handlePrompt);

const handleQuestionClick = async (event) => {
  appendAIMessage(async () => {
    const response = await fetch("/question", {
      method: "GET",
    });
    const result = await response.json();
    const question = result.answer;

    questionButton.dataset.question = question;
    questionButton.classList.add("hidden");
    questionsimple.classList.add("hidden");
    submitButton.innerHTML = "Répondre à la question";
    return question;
  });
};

questionButton.addEventListener("click", handleQuestionClick);



darkModeButton.addEventListener("click", () => {
  body.classList.toggle("dark-mode");
  if (body.classList.contains("dark-mode")) {
    darkModeButton.textContent = "White Mode";
  } else {
    darkModeButton.textContent = "Dark Mode";
  }
});

const handlesimple = async (event) => {
  appendAIMessage(async () => {
    const response = await fetch("/simplequestion", {
      method: "GET",
    });
    const result = await response.json();
    const question = result.answer;

    questionsimple.dataset.question = question;
    questionsimple.classList.add("hidden");
    questionButton.classList.add("hidden");

    submitButton.innerHTML = "Répondre à la question";
    return question;
  });
};

questionsimple.addEventListener("click", handlesimple);

document.getElementById("textButton").addEventListener("click", function () {
  window.location.href = "/pdf";
});

// document.getElementById("textButton").addEventListener("click", function () {
//   window.location.href = "/txt";
// });