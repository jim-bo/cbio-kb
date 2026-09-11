// Where the /ask page sends chat requests (the chat API's POST /api/chat).
//
// This is the only deployment-specific value in the static site. The Website
// workflow (.github/workflows/website.yml) overwrites this file before
// rendering when the repository variable CHAT_API_URL is set; otherwise the
// value below ships. An absolute URL or a same-origin path ("/api/chat") both
// work. On localhost the page ignores this and uses http://localhost:8080
// (see ask-chat.js).
window.CBIO_KB_CHAT_API_URL = "https://cbio-kb-api-7vd2hab3va-uc.a.run.app/api/chat";
