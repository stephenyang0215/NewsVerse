// Sample data structure
const data = {
    totalResults: { N: "65" },
    id: { S: "1" },
    articles: {
      L: [
        { M: { title: { S: "Title 1" }, keywords: { L: [{ S: "economy" }] } } },
        { M: { title: { S: "Title 2" }, keywords: { L: [{ S: "election" }] } } },
      ],
    },
  };
  
  // Function to display the full object
  function displayFullObject(data) {
    console.log("Complete Object:");
    console.log(JSON.stringify(data, null, 2)); // Pretty print with 2-space indentation
  }
  
  // Extract titles containing a specific keyword
  function extractTitlesByKeyword(data, keyword) {
    const results = [];
  
    if (data.articles && data.articles.L) {
      for (const article of data.articles.L) {
        const articleData = article.M;
        const title = articleData.title?.S;
        const keywords = articleData.keywords?.L.map((kw) => kw.S);
  
        if (keywords?.includes(keyword)) {
          results.push(title);
        }
      }
    }
  
    return results;
  }
  
  // Example usage
  displayFullObject(data); // Displays the full JSON object
  const keyword = "economy";
  const titles = extractTitlesByKeyword(data, keyword);
  console.log("Titles containing the keyword:", titles);
  