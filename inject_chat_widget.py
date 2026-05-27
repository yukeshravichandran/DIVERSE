import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove the static diverse-chat-branded.png image
html = re.sub(r'<img\s+src="diverse-chat-branded\.png"\s+class="hrl-hero__lead-image-5"[^>]*>', '', html)

# 2. Inject the live chat widget HTML/CSS/JS right before </body>
chat_widget_code = """
<!-- AI Chat Widget -->
<div id="ai-chat-widget">
    <div class="chat-header">
        <img src="diverse-logo.png" alt="Diverse Logo" class="chat-logo">
        <span>Diverse HR Assistant</span>
    </div>
    <div class="chat-body" id="chat-messages">
        <div class="chat-message bot">Welcome to Diverse HR. How can we assist you?</div>
    </div>
    <div class="chat-input-area">
        <input type="text" id="chat-input" placeholder="Type a message..." />
        <button id="chat-send">Send</button>
    </div>
</div>

<style>
#ai-chat-widget {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 350px;
    height: 450px;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    box-shadow: 0 15px 35px rgba(14, 165, 233, 0.2);
    display: flex;
    flex-direction: column;
    overflow: hidden;
    z-index: 999999;
    font-family: inherit;
    border: 1px solid rgba(14, 165, 233, 0.2);
}
.chat-header {
    background: linear-gradient(135deg, #0ea5e9, #0284c7);
    color: white;
    padding: 15px;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 10px;
}
.chat-logo {
    height: 24px;
    width: auto;
    filter: brightness(0) invert(1);
}
.chat-body {
    flex: 1;
    padding: 15px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.chat-message {
    padding: 10px 14px;
    border-radius: 15px;
    font-size: 14px;
    line-height: 1.4;
    max-width: 85%;
}
.chat-message.bot {
    background: #f1f5f9;
    color: #334155;
    align-self: flex-start;
    border-bottom-left-radius: 4px;
}
.chat-message.user {
    background: #0ea5e9;
    color: white;
    align-self: flex-end;
    border-bottom-right-radius: 4px;
}
.chat-input-area {
    padding: 15px;
    border-top: 1px solid #e2e8f0;
    display: flex;
    gap: 10px;
}
#chat-input {
    flex: 1;
    padding: 10px 15px;
    border: 1px solid #cbd5e1;
    border-radius: 20px;
    outline: none;
    font-family: inherit;
}
#chat-input:focus {
    border-color: #0ea5e9;
}
#chat-send {
    background: #0ea5e9;
    color: white;
    border: none;
    border-radius: 20px;
    padding: 0 15px;
    cursor: pointer;
    font-weight: 600;
}
#chat-send:hover {
    background: #0284c7;
}
.chat-message.loading {
    color: #94a3b8;
    font-style: italic;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const chatInput = document.getElementById('chat-input');
    const chatSend = document.getElementById('chat-send');
    const chatMessages = document.getElementById('chat-messages');

    function appendMessage(text, sender, isHTML=false) {
        const msgDiv = document.createElement('div');
        msgDiv.className = 'chat-message ' + sender;
        if(isHTML) {
            msgDiv.innerHTML = text;
        } else {
            msgDiv.innerText = text;
        }
        chatMessages.appendChild(msgDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
        return msgDiv;
    }

    async function sendMessage() {
        const text = chatInput.value.trim();
        if (!text) return;

        // Display user message
        appendMessage(text, 'user');
        chatInput.value = '';

        // Display loading
        const loadingDiv = appendMessage('Typing...', 'bot loading');

        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: text })
            });

            const data = await response.json();
            chatMessages.removeChild(loadingDiv);

            if (data.response) {
                // Formatting links and bold text
                let formattedText = data.response
                    .replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>')
                    .replace(/\\n/g, '<br>');
                appendMessage(formattedText, 'bot', true);
            } else {
                appendMessage('Sorry, I encountered an error.', 'bot');
            }
        } catch (error) {
            chatMessages.removeChild(loadingDiv);
            appendMessage('Connection error. Please try again later.', 'bot');
        }
    }

    chatSend.addEventListener('click', sendMessage);
    chatInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') sendMessage();
    });
});
</script>
"""

# Find the closing </body> tag and inject before it
if "<!-- AI Chat Widget -->" not in html:
    html = html.replace("</body>", chat_widget_code + "\n</body>")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Live chat widget injected!")
