import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="newsdb"
)

cursor = mydb.cursor() 
 
# Execute the SELECT statement 
cursor.execute("SELECT * FROM news") 
 
# Fetch the data 
data = cursor.fetchall() 
 
# Create an HTML table 
html = "<table>\n" 
html += "<tr>\n" 
html += "<th>column_1</th>\n" 
html += "<th>column_2</th>\n" 
html += "<th>column_3</th>\n" 
html += "</tr>\n" 
for row in data: 
    html += "<tr>\n" 
    html += "<td>{}</td>\n".format(row[0]) 
    html += "</tr>\n" 
html += "</table>" 
 
# Close the cursor and connection 
cursor.close() 
mydb.close() 
 
# Print the HTML table 
print(html)