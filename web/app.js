const form = document.getElementById("chatForm");
const input = document.getElementById("userInput");
const messages = document.getElementById("messages");

// Create one session ID per browser tab
const sessionId = crypto.randomUUID();

function addMessage(text, who){
  const row = document.createElement("div");
  row.className = `msg ${who}`;
  const bubble = document.createElement("div");
  bubble.className = "bubble";
  bubble.textContent = text;
  row.appendChild(bubble);
  messages.appendChild(row);
  messages.scrollTop = messages.scrollHeight;
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const msg = input.value.trim();
  if(!msg) return;

  addMessage(msg, "usermsg");
  input.value = "";

  const thinking = document.createElement("div");
  thinking.className = "msg botmsg";
  thinking.innerHTML = `<div class="bubble">Thinking...</div>`;
  messages.appendChild(thinking);
  messages.scrollTop = messages.scrollHeight;

  try{
    const res = await fetch("/chat", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        message: msg,
        session_id: sessionId   // 👈 send session id
      })
    });

    const data = await res.json();
    thinking.remove();
    addMessage(data.answer || "No answer returned.", "botmsg");

  } catch(err){
    thinking.remove();
    addMessage("Server error. Check backend logs.", "botmsg");
  }
});
