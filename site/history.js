document.addEventListener("DOMContentLoaded", function () {
    // Sample test data (replace this with your actual data)
    const testData = [
      {
        oldStatus: "old",
        newStatus: "gate",
        lastTimeChanged: "23-11-01 10:25:52.935709",
      },
      {
        oldStatus: "old",
        newStatus: "gate",
        lastTimeChanged: "23-11-01 10:26:00.996843",
      },
      // Add more sample data here
    ];
  
    // Inside your renderSampleTable function
    function renderSampleTable(data) {
        // Create an HTML table to display the data with styles
        let tableHTML = "<table style='border: 1px solid;height: 150px;padding: 15px;'>";
        tableHTML += "<tr><th>Old Status</th><th>New Status</th><th>Last Time Changed</th></tr>";

        data.forEach(function (entry) {
            tableHTML += "<tr>";
            tableHTML += "<td>" + entry.oldStatus + "</td>";
            tableHTML += "<td>" + entry.newStatus + "</td>";
            tableHTML += "<td>" + entry.lastTimeChanged + "</td>";
            tableHTML += "</tr>";
        });

        tableHTML += "</table>";

        // Update the content of the history log element
        const historyLogElement = document.getElementById("history-log");
        historyLogElement.innerHTML = tableHTML;
    }


          // Call the function with the test data
        renderSampleTable(testData);
      
  });
  