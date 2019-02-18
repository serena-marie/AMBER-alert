# AMBER-alert
A group project for **CS4347: Introduction to Machine Learning**.

This project was divided into three parts:
- Object Identification by J. Hope
- Model Identification by L. Anseti
- **Color Identification** by Serena Gutierrez


As of Feb. 2019, this code identifies Silver, White, Black, Blue, Green, Yellow, Orange, and Red. It does not identify multi-toned vehicles (i.e. vehicle with a stripe.) Currently, reconsidering some implementation choices but will research more into it when I have some more leisure time. 

While the program correctly identifies the dominate color, using K-Means, the real challenge is naming the color. As seen in images below, vehicles that are silver, black, or white (the 3 most common car colors) are difficult to classify because they are very close. 

This is an incomplete repository. 
## Still to complete
- [x] Identify all [common] colors
- [ ] Object Identification
- [ ] Model Identification

<img src="https://github.com/serena-marie/AMBER-alert/blob/master/readme_images/black_scatter.png" width="275" height="300" alt="Black Scatterplot"> <img src="https://github.com/serena-marie/AMBER-alert/blob/master/readme_images/silver_scatter.png" width="275" height="300" alt="Silver Scatterplot"> <img src="https://github.com/serena-marie/AMBER-alert/blob/master/readme_images/white_scatter.png" width="275" height="300" alt="White Scatterplot">
Scatterplots: Black Vehicle, Silver Vehicle, and White Vehicle
