function clickCancelButtonsWithRandomDelay() {
    const buttons = document.querySelectorAll('button');
  
    function getRandomDelay() {
      return Math.floor(Math.random() * 3000) + 2000;
    }
  
    async function clickWithDelay(button, delay) {
      await new Promise(resolve => setTimeout(resolve, delay));
      button.click();
    }
  
    for (const button of buttons) {
      if (button.textContent.includes("Friends")) {
        const randomDelay = getRandomDelay();
        clickWithDelay(button, randomDelay);

        const unfriend_button = document.querySelector('span');
        if (unfriend_button.textContent.includes("Unfriend")) {
          clickWithDelay(unfriend_button, 100);
        }
        
      }
    }
  }
  
  clickCancelButtonsWithRandomDelay();