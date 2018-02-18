import dash
import dash_core_components as dcc
import dash_html_components as html


from Rom_figures import corr
from Rom_figures import gdp
from Rom_figures import dopc
from Rom_figures import dopct
from Rom_figures import srm

app=dash.Dash()

app.css.append_css({"external_url": 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

app.layout=html.Div([

	#Part1

	html.Div([

		html.H1(children="Homework 3", style={"color":"brown", "text-align":"center", "font-family":"Helvetica",})],
		className="twelve columns"),

		html.Div([
			html.Div([html.P("Homework 3 assumes the development of this web application using Dash and Plotly in Python. You are required to develop 6 plots (including one table) with the given layout. Subtle differences related to styling (colors etc) are allowed, yet the general layout must be kept to perceive same information as this website does. Quandl is used as a data source for 4 plots among 6, while the other 2 are based on user provided data. Some of the Quandl based plots require minor analysis using pandas. You are encouraged to follow below mentioned steps to complete the HW:",
				style={"text-align":"justify","padding-left":"15",}), 
				html.Ol([
					html.Li("Start from first developing the 6 plots in Jupyter Notebook,"),
					html.Li("Once plots are ready post them into the Dash app,"), 
					html.Li("Add HTML components (website heading etc.),"),
					html.Li("Structure the layout of the dashboard.")
					], style={"padding-left":"20",})
					
				], className="four columns"),

			html.Div([html.P("Graph 1", style={"font-weight":"bold",}), 
				html.P("The graph on the right hand side is showing correlations of different variables (call them from x1 to x8) with employee churn. Data is artificial, manually inputted by the developer. Recreate the graph. Small coloring or corelation value differences will be neglected"), 
				], className="four columns"),

			html.Div([
			dcc.Graph(id="Graph1", figure=corr)],
			className="four columns"),


			], className="twelve columns"),
		#Part2

		html.Div([
			html.Div([html.P("Graph 2", style={"font-weight":"bold",}), 
				html.P("One the right hand side we have US GDP graphed over time. The data is sourced from QUANDL API (FRED/GDP). Your task is to recreate exactly the same graph.", style={"text-align":"justify", "padding-left":"10",}), 
				], className="four columns"),

			html.Div([dcc.Graph(id="Graph2", figure=gdp)],
			className="six columns"),


			html.Div([],
			className="two columns"),


			], className="twelve columns"),

		#Part3

		html.Div([
			html.Div([html.P("Graph 3 and 4", style={"font-weight":"bold",}), 
				html.P("The two graphs on this row are based on Google's stock (WIKI/GOOGL) and Bitcoin's (BCHARTS/ABUCOINSUSD) prices sourced from Quandl. First, percentage changes are calculated. Then the latter is plotted using Box plot to find the distribution and outliers. In the end the first 4 percentage changes (apart from the very first one, which is N/A) are plotted in a table. Recreate similar graphs with the same values (minor styling is neglected)."), 
				], className="four columns"),

			html.Div([
			dcc.Graph(id="Graph 3", figure=dopc)],
			className="four columns"),

			html.Div([
			dcc.Graph(id="Graph 4", figure=dopct)],
			className="four columns")
				
			], className="twelve columns"),


		#Part4
		
		html.Div([
			html.Div([html.P("Graph 5", style={"font-weight":"bold",}), 
				html.P("Last graph is based on manually inputted data. It shows the Roadmap developed by an artificial startup. Task 1 is assumed to take the whole Janduary, while Task 2 is starting from March and ending in mid April. Afterwards, Task 3 begins and ends in the end of September. Recreate a similar Roadmap.", style={"text-align":"justify", "padding-left":"10",}), 
				], className="four columns"),

			html.Div([
			html.H5(),
			dcc.Graph(id="Graph5", figure=srm)],
			className="six columns"),



			html.Div([],
			className="two columns")


			], className="twelve columns")
	
		
		])	

if __name__=='__main__':
		app.run_server(debug=True)








		