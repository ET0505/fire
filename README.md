# FIRE
FIRE is a web-based application that enables users to calculate their unique timeline of investing to live the FIRE (Financial Independence, Retire Early) lifestyle. It calculates the projected returns based on the $F = P + ([A(r + 1)^t - 1] / r)$ formula and provides an estimation, assuming consistent investments over the long term. 

This application was developed as a passion project, combining my interests in full-stack development and personal finance. Through my own financial journey, I discovered that setting measurable goals and celebrating the small wins are essential for maintaining motivation and ensuring consistent progress. Inspired by this experience, I developed this tool to visualise my personal timeline and support others to succeed. Enjoy using this application and good luck on your journey!. https://fire-app-81d5e62b8231.herokuapp.com/

## Functionalities 
Users can select their investment frequency and input the following:
- Principle amount
- Goal amount
- Investment amount
- Growth rate of investments

The application will calculate 10%, 25% 33%, 50%, and 75% of the goal and output the timeframe required to achieve those milestones. It will also display the projected contributions and returns on a histogram for easy visualisation.

## Tech stack
**Backend:** Python, Django
- **Python:** Used to create the main program which renders the template and performs the calculations from the input.
- **Django:** A Python web framework that enables the web application to be deployed to a development server for testing.

**Frontend:** HTML, CSS, JavaScript
- **HTML:** Basic structure and template of the web page.
- **CSS:** Style the components on the web page.
- **JavaScript:** Include functionalities for components that are present on the web page.

## Folders and Files
- static
  - `style.css` - A CSS file that is used to style the contents of the web application.
  - Images - Include the logo for the web application and icons for the links. 
- templates
  - `home.html` - An HTML file that serves as the home page for the web application.
- `views.py` - A Python file that defines functions to render the template HTML page and calculate the output based on input from the POST method. 

## How to run
1. Ensure that you have installed the required technologies, libraries, and frameworks.
2. Run the program by running the command `python manage.py runserver` in the terminal.

## Learnings
Taking on this project pushed me to explore different technologies, many of which were new to me. For this project, I used Django as a web framework which gave me the chance to see how it was different to Flask. I also learned to implement AJAX to dynamically update the web page, rather than rendering the entire page with each update. Understanding how this worked with the backend through the POST method was enlightening and was a significant learning experience. 

Moreover, I also wanted to visualise the projections through a graph, and so I picked up Chart.js to render the histogram. Ultimately, this project encouraged me to learn new technologies and approaches, which I am excited to apply in future projects.

## Future Considerations
The application functions as intended, but there are a few areas for improvement. For instance, adding an option for fortnightly frequencies could enhance customisation for an improved user experience. Additionally, taking into account other variables such as inflation can provide a more realistic projection of returns. I also plan to improve the accuracy of the projected estimations for longer timeframes.

I would also love to hear your thoughts, so do not hesitate to give your feedback!
