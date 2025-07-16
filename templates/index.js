const editor = ace.edit("editor");
editor.setTheme("ace/theme/github");
editor.session.setMode("ace/mode/python");
editor.setValue("print('Hello, Cody!')", 1);
editor.setOptions({ fontSize: "14px", useWorker: false });

let isDark = false;

function toggleTheme() {
  isDark = !isDark;
  editor.setTheme(isDark ? "ace/theme/monokai" : "ace/theme/github");
  document.getElementById('body').className = isDark ? "bg-gray-900 text-gray-100" : "bg-gray-100 text-gray-800";
}

function changeLang(lang) {
  editor.session.setMode("ace/mode/" + lang);
  if (lang === "python") {
    editor.setValue("print('Hello, Cody!')", 1);
  } else {
    editor.setValue("console.log('Hello, Cody!');", 1);
  }
}

function copyCode() {
  navigator.clipboard.writeText(editor.getValue()).then(() => {
    alert("Code copied to clipboard!");
  });
}

function runCode() {
  const language = document.getElementById("language").value;
  const code = editor.getValue();

  const payload = {
    language: language,
    code: code
  };

  fetch("http://192.168.1.5:5000/api/v1/cody", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  })
  .then(response => response.json())
  .then(data => {
    if (data.output) {
      alert("✅ Output:\\n\\n" + data.output);
    } else if (data.error) {
      alert("❌ Error:\\n\\n" + data.error);
    } else {
      alert("⚠️ Unknown response.");
    }
  })
  .catch(err => {
    alert("❌ Request failed:\\n" + err.message);
  });
}
