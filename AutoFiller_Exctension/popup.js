document.addEventListener("DOMContentLoaded", async () => {
  const res = await fetch(chrome.runtime.getURL("clients.json"));
  const clients = await res.json();

  const dropdown = document.getElementById("clientSelect");
  Object.keys(clients).forEach(name => {
    const option = document.createElement("option");
    option.value = name;
    option.textContent = name;
    dropdown.appendChild(option);
  });

  document.getElementById("fillForm").addEventListener("click", () => {
    const selected = dropdown.value;
    if (selected && clients[selected]) {
      chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.scripting.executeScript({
          target: { tabId: tabs[0].id },
          func: (client) => {
            const fieldMap = {
              "First Name": "first_name",
              "Last Name": "last_name",
              "DOB": "dob",
              "Aadhar Number": "aadhar_number",
              "Mobile Number": "mobile_number",
              "Gmail ID": "email",
              "PAN Number": "pan_number",
              "Address": "address",
              "Bank Account Number": "bank_account",
              "IFSC Code": "ifsc_code"
            };

            for (const key in client) {
              const fieldName = fieldMap[key] || key;
              const input = document.querySelector(`input[name='${fieldName}'], textarea[name='${fieldName}']`);
              if (input) {
                input.value = client[key];
              } else {
                console.warn("No input found for:", fieldName);
              }
            }
          },
          args: [clients[selected]]
        });
      });
    }
  });
});
