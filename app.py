import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff
import streamlit as st
import functions

df1 = pd.read_csv("IPL_Ball_by_Ball_2008_2022.csv")
df2 = pd.read_csv("IPL_Matches_2008_2022.csv")

#st.sidebar.title("This is IPL Analysis Project.")
#st.sidebar.title("   IPL Data Analysis")

hide_main_menu_style = """
<style>
#MainMenu .menu-item {
    display: none !important;
}
</style>
"""

st.markdown(hide_main_menu_style, unsafe_allow_html=True)

st.sidebar.markdown(
    '<div style="text-align: center; font-size: 35px; font-weight: bold;">IPL DATA ANALYSIS</div>',
    unsafe_allow_html=True
)

with st.sidebar:
    col1, col2, col3 = st.columns(3)

    url1 = "https://github.com/ajstyle007"
    text1 = "Github" 

    url2 = "https://medium.com/p/c38b78239e4f/edit"
    text2 = "Blog Post" 

    url3 = "https://www.linkedin.com/in/ajay-kumar-72ba861b8/"
    text3 = "Linkedin"

    col1.link_button(text1, url1)
    col2.link_button(text2, url2)
    col3.link_button(text3, url3)

st.sidebar.image("ipl.jpg", width = 220)
#st.table(df1.head())
user_menu = st.sidebar.radio("Select an option", ("Overview", "Player Statistics", "Team wise Analysis", "Players wise Analysis", "miscellaneous analysis"))

if user_menu == "Overview":
    #st.markdown("<center><font size='6'><b>IPL Exploratory Data Analysis</b></font></center>", unsafe_allow_html=True)
    col1, col2, col3, col4,col5, col6 = st.columns([5,1,1,2,3,3])
    with col1:
        st.image("IPL_new.png", width=400)

    with col4:
        st.markdown("### :cricket_bat_and_ball:")
        st.markdown("### :softball:")
        st.markdown("### :cricket_bat_and_ball:")
        st.markdown("### :softball:")
        st.markdown("### :cricket_bat_and_ball:")
        st.markdown("### :softball:")
        st.markdown("### :cricket_bat_and_ball:")
        st.markdown("### :softball:")
    with col5:
        season = df2["Season"].nunique()
        st.markdown("##### :green[Seasons] :sports_medal:")
        st.header(season)

        total_wick = df1[df1["isWicketDelivery"] == 1]["bowler"].value_counts().sum()
        st.markdown("##### :green[Wickets] :cricket:")
        st.header(total_wick)

        sixes = df1[df1["batsman_run"] == 6]["batsman_run"].count()
        st.markdown("##### :green[Total 6s] :six:")
        st.header(sixes)

        merd_df = pd.merge(df1, df2, how='inner', on='ID')
        hunderds = merd_df.groupby(["ID", "batter"])["batsman_run"].sum().reset_index()
        hun_100 = hunderds[hunderds["batsman_run"] >= 100]["batsman_run"].count()
        st.markdown("##### :green[Total 100s] :100:")
        st.header(hun_100)
    
    with col6:
        b_run = df1[df1["batsman_run"] >= 1]
        top_10_bats = b_run.groupby("batter")["batsman_run"].sum().sum()
        st.markdown("##### :green[Runs] :cricket_bat_and_ball:")
        st.header(top_10_bats)

        total_balls = df1.shape[0]
        st.markdown("##### :green[Balls] :softball:")
        st.header(total_balls)

        fours = df1[df1["batsman_run"] == 4]["batsman_run"].count()
        st.markdown("##### :green[Total 4s] :four:")
        st.header(fours)

        merd_df = pd.merge(df1, df2, how='inner', on='ID')
        fift = merd_df.groupby(["ID", "batter"])["batsman_run"].sum().reset_index()
        hun_50 = fift[(fift["batsman_run"] >= 50) & (fift["batsman_run"] <100)]["batsman_run"].count()
        st.markdown("##### :green[Total 50s] :five::zero:")
        st.header(hun_50)

    
    #     st.markdown("<div style='border-left: 2px solid #FFF; height: 100px;'></div>", unsafe_allow_html=True)
    expander = st.expander("About")
    with expander:
        st.write("""This is a homepage of the web app serves as an overview dashboard, 
            showcasing key metrics summarizing the IPL dataset. Here, 
            users can immediately grasp important statistics such as the total runs scored, 
            total balls bowled, total wickets taken, number of seasons played,
            the total number of sixes and fours hit, as well as the count of 
            centuries and half-centuries scored throughout IPL history.""")
                 
        st.write("""Additionally, a sidebar is prominently featured with 
            five radio buttons labeled "Overview," "Player Statistics," 
            "Player-Wise Analysis," "Team-Wise Analysis," and 
            "Miscellaneous Analysis." These radio buttons act as navigation tools, 
            enabling users to delve deeper into specific aspects of IPL data analysis.
            Clicking on any of these buttons directs users to dedicated sections 
            within the web app, where they can explore detailed visualizations 
            and in-depth analysis tailored to their chosen category of interest. 
            This intuitive design facilitates seamless exploration and enhances 
            user experience, allowing cricket enthusiasts to uncover insights and 
            trends within the rich landscape of IPL data.""")

if user_menu == "Player Statistics":
    #st.title("Player Statistics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("images.jpg", width = 130)
    with col2:
        html_content = f"<h1 style='text-align: center; color: cyan; font-size: 70px;'>PLAYER</h1><br>"
        st.markdown(html_content, unsafe_allow_html=True)
    with col3:
        html_content = f"<h1 style='text-align: center; color: cyan; font-size: 70px;'>Statistics</h1><br>"
        st.markdown(html_content, unsafe_allow_html=True)
        

    batter_list = df1["batter"].sort_values().unique().tolist()
    #batter_list = batter_list
    player_name = st.selectbox("Select a player name", batter_list)
    functions.player_statistics(player_name)

    Total_runs = functions.player_statistics(player_name)[0]
    Total_balls_faced = functions.player_statistics(player_name)[1]
    Batting_avg = functions.player_statistics(player_name)[2]
    Strike_rate = functions.player_statistics(player_name)[3]
    total_matches_played = functions.player_statistics(player_name)[4]
    total_50 = functions.player_statistics(player_name)[5]
    total_100 = functions.player_statistics(player_name)[6]
    total_4 = functions.player_statistics(player_name)[7]
    total_6 = functions.player_statistics(player_name)[8]
    total_3 = functions.player_statistics(player_name)[9]
    high_score = functions.player_statistics(player_name)[10]
    total_0 = functions.player_statistics(player_name)[11]
    total_wickets = functions.player_statistics(player_name)[12]
    total_balls_throw = functions.player_statistics(player_name)[13]
    total_runs_conceded = functions.player_statistics(player_name)[14]
    bowling_average = functions.player_statistics(player_name)[15]
    total_catches = functions.player_statistics(player_name)[16]
    five_wickets = functions.player_statistics(player_name)[17]
    four_wickets = functions.player_statistics(player_name)[18]

    col1, col2, col3 = st.columns(3)
    with col2:
        st.title(f" :rainbow[{player_name}]")
    # st.markdown("""
    #     <div style="border: 2px solid #3498db; border-radius: 5px; padding: 10px; background-color: #f2f2f2; text-align: center;">
    #         <p style="color: #3498db; font-size: 18px; font-weight: bold;">V Kohli</p>
    #     </div>
    # """, unsafe_allow_html=True)
    # Use st.info, st.success, st.warning, or st.error to create different styled boxes

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.subheader("Runs") 
        st.title(Total_runs)
    with col2:
        st.subheader("Balls faced")
        st.title(Total_balls_faced)
    with col3:
        st.subheader("Strike Rate")
        st.title(round(Strike_rate,2))
        
    with col4:
        st.subheader("Batting Average")
        st.title(round(Batting_avg,2))

    st.markdown("***")

    col1, col2, col3,col4 = st.columns(4)

    with col1:
        st.subheader("Wickets")
        st.title(total_wickets)
    with col2:
        st.subheader("Balls throw")
        st.title(total_balls_throw)
    with col3:
        st.subheader("Runs conceded")
        st.title(total_runs_conceded)
        
    with col4:
        st.subheader("Bowling Average")
        st.title(round(bowling_average,2))

    st.markdown("***")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.subheader("Matches played")
        st.title(total_matches_played)
    with col2:
        st.subheader("High Score")
        st.title(high_score)
    with col3:
        st.subheader("Catches")
        st.title(total_catches)
    with col4:
        st.subheader("5 Wickets")
        st.title(five_wickets)

    st.markdown("***")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.subheader("50s")
        st.title(total_50)
    with col2:
        st.subheader("100s")
        st.title(total_100)
    with col3:
        st.subheader("4s")
        st.title(total_4)
    with col4:
        st.subheader("6s")
        st.title(total_6)

    st.markdown("***")

    play_out = df1.groupby(["player_out", "kind"])["player_out"].count().reset_index(allow_duplicates=True)
    play_out.columns = play_out.columns.to_series().mask(play_out.columns.duplicated(), lambda x: "out").tolist()
    player_out_df = play_out[play_out["player_out"] == player_name].sort_values("out", ascending=False).reset_index(drop=True)[["kind", "out"]]

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader("3s")
        st.title(total_3)

    with col2:
        st.subheader("0s")
        st.title(total_0)
    with col3:
        st.subheader("4 wickets")
        st.title(four_wickets)
    with col4:
        st.subheader("Kind of outs")
        st.table(player_out_df)
    

    expander1 = st.expander("See Explanation")
    with expander1:
        st.write("""Above is a simple function using the IPL dataset 
                 that retrieves all the basic information about an IPL player. 
                 This function allows users to input the 
                 player's name and receive essential details such as their team, 
                 batting and bowling averages, strike rates, and other relevant stats. 
                 It's a convenient tool for quickly accessing key information about any 
                 IPL player from the dataset.""")


if user_menu == "Team wise Analysis":

    tab1, tab2 = st.tabs(["Analysis 1", "Analysis 2"])
    # n_df = df.drop_duplicates(subset="Year")[["Year","City"]]
    # fig = px.bar(n_df, x='City', y='Year',text_auto = True,)
    # fig.update_xaxes(tickangle=45)
    # st.plotly_chart(fig)

    with tab1:

        team_runs = df1.groupby("BattingTeam")["batsman_run"].sum().reset_index()
        team_runs.rename(columns={"batsman_run":"Total_runs"}, inplace=True)
        fig = px.scatter(team_runs, x="BattingTeam", y="Total_runs",size="Total_runs", color="BattingTeam", size_max=65)
        for i, value in enumerate(team_runs['Total_runs']):
            fig.add_annotation(
                x=team_runs['BattingTeam'][i],
                y=value,
                text=str(value), showarrow=False, bgcolor="black")
        fig.update_layout(title = "Total Runs by IPL Teams",title_x=0.35,title_y=0.95, width=1000, height=550)
        st.plotly_chart(fig)

        st.markdown("****")

        newdf = df2["Team2"].value_counts() + df2["Team1"].value_counts()
        newdf1 = pd.DataFrame(newdf).reset_index()
        newdf1.rename(columns={"index": "teams"}, inplace=True)

        #("Total match played by the each teams")
        fig = px.bar(newdf1, x='teams', y='count')
        
        for i, value in enumerate(newdf1['count']):
            fig.add_annotation(
                x=newdf1['teams'][i],
                y=value,
                text=str(value), showarrow=False, bgcolor="black")
        fig.update_layout(title = "Total Matches played by the each team",title_x=0.3,title_y=0.9, autosize=False, width=900,height=400)
        st.plotly_chart(fig)

        st.markdown("****")

        teams_count = df2.groupby("Season")["Team1"].nunique().reset_index()
        fig = px.scatter(teams_count, x = "Season", y = "Team1", size = "Team1", size_max=60, color=teams_count["Team1"])
        for i, value in enumerate(teams_count['Team1']):
            fig.add_annotation(
                x=teams_count['Season'][i],
                y=value,
                text=str(value), showarrow=False, bgcolor="black")
        fig.update_layout(title = "Total teams participating over the years",title_x=0.3,title_y=0.9, autosize=False, width=900,height=500)
        st.plotly_chart(fig)

        st.markdown("****")

        col1, col2, col3 = st.columns(3)
        with col2:
            st.markdown("**<font size='4'>Total matches win by the teams**</font>", unsafe_allow_html=True)
            #<font size='5'>This is bold text with custom size</font>
        col1, col2 = st.columns(2)
        with col1:
            win_df = df2["WinningTeam"].value_counts().reset_index()
            st.table(win_df)
        
        with col2:
            fig = px.pie(win_df, values="count", names = "WinningTeam")
            fig.update_layout(autosize=False, width=500,height=600)
            st.plotly_chart(fig)

        st.markdown("****")

        win_teams_df = df2[df2["MatchNumber"]=="Final"]
        final_win = win_teams_df["WinningTeam"].value_counts().reset_index()
        fig = px.bar(final_win, x='WinningTeam', y='count')
        for i, value in enumerate(final_win['count']):
            fig.add_annotation(
                x=final_win['WinningTeam'][i],
                y=value,
                text=str(value), showarrow=False, bgcolor="black")
        fig.update_layout(title = "Total final wins by the teams",title_x=0.4,title_y=0.9, autosize=False, width=900,height=400)
        fig.update_traces(marker_color = 'green', marker_line_color = 'black',marker_line_width = 2, opacity = 1)
        st.plotly_chart(fig)

        st.markdown("****")
        finals = df2[df2["MatchNumber"] == "Final"]
        most_finals = finals["Team1"].tolist() + finals["Team2"].tolist()
        most_final_play = pd.DataFrame(most_finals).value_counts().reset_index()
        most_final_play.rename(columns={0:"teams", "count":"count"}, inplace=True)
        fig = px.bar(most_final_play, x='teams', y='count')
        for i, value in enumerate(most_final_play['count']):
            fig.add_annotation(
                x=most_final_play['teams'][i],
                y=value,
                text=str(value), showarrow=False, bgcolor="black")
        fig.update_layout(title = "Most Finals played by the teams",title_x=0.4,title_y=0.9, autosize=False, width=900,height=400)
        fig.update_traces(marker_color = 'yellow', marker_line_color = 'black',marker_line_width = 2, opacity = 1)
        st.plotly_chart(fig)
        
        
    
    with tab2:

        city_match = df2["City"].value_counts().reset_index()
        fig = px.bar(city_match, x = "City", y = "count", text="count", width=1000, height=600)
        fig.update_layout(title = "Name of the matches hosted in different cities", title_x=0.3,title_y=0.9, 
                          autosize=False, width=900,height=400, barmode='group', xaxis_tickangle=-45)
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside', marker_color = 'red', marker_line_color = 'black')
        st.plotly_chart(fig)

        st.markdown("****")

        st.markdown("<center><font size='3'><b>Win percentage as batting team and bowling team</b></font></center>", unsafe_allow_html=True)
        
        col1, col2= st.columns(2)
        with col1:

            win_bat = (df2.Team1 == df2.WinningTeam)
            win_bat1 = win_bat.value_counts().reset_index()
            fig = px.pie(win_bat1, names="index", values="count")
            fig.update_layout(title = "Win percentage as batting team", title_x=0.3,title_y=0.1, 
                              legend=dict(yanchor="top", y=0.9, xanchor="right", x=0.2), 
                              autosize=False, width=600,height=400, barmode='group', xaxis_tickangle=-45)

            st.plotly_chart(fig)

        with col2:

            win_field = (df2.Team2 == df2.WinningTeam)
            win_field1 = win_field.value_counts().reset_index()
            fig = px.pie(win_field1, names="index", values="count")
            fig.update_layout(title = "Win percentage as bowling team", title_x=0.28,title_y=0.1, 
                              legend=dict(yanchor="top", y=0.9, xanchor="right", x=0.2),
                                autosize=False, width=600,height=400, barmode='group', xaxis_tickangle=-45)

            st.plotly_chart(fig)
        st.markdown("****")

        st.markdown("<center><font size='3'><b>Matches Played vs Matches Won by the teams</b></font></center>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:

            team_con = pd.concat([df2["Team1"], df2["Team2"]])
            played_df = team_con.value_counts().reset_index()
            played_df.columns = ["teams", "played_count"]
            played_df["winning_count"] = df2["WinningTeam"].value_counts().reset_index()["count"]
            st.table(played_df)

        with col2:

            win_percentage = (df2["WinningTeam"].value_counts() / team_con.value_counts()*100).sort_values(ascending=False).reset_index()
            fig = px.pie(win_percentage, names="index", values="count")
            fig.update_layout(autosize=False, width=550,height=800)
            st.plotly_chart(fig)
            #legend=dict(yanchor="top", y=1, xanchor="left", x=0, font = dict(size=12)),
        st.markdown("****")

        col1, col2, col3,col4 = st.columns(4)

        with col2:
            win_toss = (df2.WinningTeam == df2.TossWinner)
            win_toss1 = win_toss.value_counts().reset_index()
            fig = px.pie(win_toss1, names="index", values="count", hole=.4, color_discrete_sequence=px.colors.sequential.RdBu)
            fig.update_layout(title = "Win Toss Win Match Analysis", title_x=0.25,title_y=1,
                              annotations=[dict(text='WTWM', x=0.5, y=0.5, font_size=17, showarrow=False)], 
                              legend=dict(yanchor="top", y=1, xanchor="left", x=-0.2),autosize=False, width=500,height=450)
            st.plotly_chart(fig)

        st.markdown("****")

        from plotly.subplots import make_subplots
        margin_df = df2[["WinningTeam", "WonBy", "Margin"]]
        won_by_wickets = margin_df[margin_df["WonBy"] == "Wickets"]
        won_by_runs = margin_df[margin_df["WonBy"] == "Runs"]
        fig = make_subplots(rows=2, cols=1, subplot_titles=("Win Margin of Teams Won by Runs", "Win Margin of Teams Won by Wickets"))
        fig.add_trace(px.scatter(won_by_runs, x="WinningTeam", y="Margin", color="Margin").data[0], row=1, col=1)
        fig.add_trace(px.scatter(won_by_wickets, x="WinningTeam", y="Margin", color="Margin").data[0], row=2, col=1)
        fig.update_layout(width=1000, height=800)
        st.plotly_chart(fig)

    expander2 = st.expander("See Explanation")
    with expander2:
        st.write("""In the "Team-Wise Analysis" section, users can explore IPL team performance 
                 through two tabs: "Analysis 1" and "Analysis 2." 
                 These tabs offer distinct insights into various metrics and trends, 
                 enabling users to gain a comprehensive understanding of team dynamics.Like""")
        message = """* Total Runs by IPL Teams 
                 * Total Finals Wins by the teams
                 * Total Matches win by the Teams
                 * Total Matches played by each team
                 * Total teams participating over the years
                 * Most Finals played by the teams
                 * Win Toss-Win Match Analysis
                 * Most Finals played by the Teams
                 * Number of Matches hosted in different cities
                 * Win percentage as batting team and bowling team 
                 * Matches played vs Matches Won by the teams
                 * Win Margin of teams Won by runs and by Wickets"""
        lines = message.split("\n")

        # Print each line in the list
        for line in lines:
            st.write(line)

if user_menu == "Players wise Analysis":

    tab1, tab2 = st.tabs(["Analysis 1", "Analysis 2"])

    with tab1:
        orange_cap = functions.orange_cap_holder(df1, df2)
        orange_cap["Season_run"] = orange_cap["Season"].astype("str") + "=>" + orange_cap["batsman_run"].astype("str")
        #st.table(orange_cap.reset_index(drop=True))

        fig = px.bar(orange_cap, x='batter', y='Season_run',text_auto = True)
        fig.update_xaxes(tickangle=45)
        fig.update_layout(title = "Orange Cap Holders 2008-2022",title_x=0.4,title_y=1, width=850, height=430)
        fig.update_traces(marker_color = 'orange', marker_line_color = 'black',marker_line_width = 2, opacity = 1)
        st.plotly_chart(fig)

        st.markdown("****")

        purple_cap = functions.purple_cap_holder(df1, df2)
        purple_cap["Season_wickets"] = purple_cap["Season"].astype("str") + "=>" + purple_cap["isWicketDelivery"].astype("str")

        #st.table(purple_cap.reset_index(drop=True))

        fig = px.bar(purple_cap, x='bowler', y='Season_wickets', text_auto=True)
        fig.update_xaxes(tickangle=45)
        fig.update_layout(title = "Purple Cap Holders 2008-2022",title_x=0.4,title_y=1, width=900, height=400)
        fig.update_traces(marker_color = 'purple', marker_line_color = 'black',marker_line_width = 2, opacity = 1)
        st.plotly_chart(fig)
    
        st.markdown("****")

        total_hun = functions.top_10_hunderds(df1, df2)
        fig = px.bar(total_hun, x='count', y='batter', orientation="h", text_auto=True)
        fig.update_xaxes(tickangle=45)
        fig.update_layout(title = "Most 100s by a Batsman 2008-2022",title_x=0.4,title_y=1, width=900, height=400)
        fig.update_traces(marker_color = total_hun["count"], marker_line_color = 'black',marker_line_width = 2, opacity = 1)
        st.plotly_chart(fig)

        st.markdown("****")

        most_6 = functions.most_sixes(df1)
        fig = px.funnel(most_6, x = "batter", y='count')
        fig.update_xaxes(tickangle=45)
        fig.update_layout(title = "Most 6s by a Batsman 2008-2022",title_x=0.4,title_y=1, width=900, height=400)
        fig.update_traces(marker_color = 'cyan', marker_line_color = 'black',marker_line_width = 2, opacity = 1)
        st.plotly_chart(fig)

        st.markdown("****")

        catches_df = df1[df1["kind"] == "caught"]["fielders_involved"].value_counts().head(20).reset_index()
        fig = px.scatter(catches_df, x="fielders_involved", y="count",size="count", color="fielders_involved", size_max=45)
        for i, value in enumerate(catches_df['count']):
            fig.add_annotation(
                x=catches_df['fielders_involved'][i],
                y=value,
                text=str(value), showarrow=False, bgcolor="black")
        fig.update_layout(title = "Most Catches by a player",title_x=0.35,title_y=0.95, width=1000, height=450)
        fig.update_traces(marker_line_color = 'black',marker_line_width = 0.5, opacity = 1)
        st.plotly_chart(fig)

        

    with tab2:

        aj = functions.top_10_batsman(df1)
        fig = px.bar(aj, x = "batter", y = "batsman_run")
        for i, value in enumerate(aj['batsman_run']):
            fig.add_annotation(
                x=aj['batter'][i],
                y=value,
                text=str(value), showarrow=False, bgcolor="black")
        fig.update_layout(title = "Top 10 batsmans by runs",title_x=0.4,title_y=1, width=900, height=400)
        fig.update_traces(marker_color = 'red', marker_line_color = 'black',marker_line_width = 2, opacity = 1)
        st.plotly_chart(fig)
    
        st.markdown("****")

        wick = functions.top_10_wick(df1)
        fig = px.bar(wick, x = "bowler", y = "count")
        for i, value in enumerate(wick['count']):
            fig.add_annotation(
                x=wick['bowler'][i],
                y=value,
                text=str(value), showarrow=False, bgcolor="black")
        fig.update_layout(title = "Top 10 wicket takers in IPL 2008-2022",title_x=0.35,title_y=1, width=900, height=400)
        fig.update_traces(marker_color = 'green')
        st.plotly_chart(fig)

        st.markdown("****")

        mbf = functions.max_balls_faced(df1)
        fig = px.bar(mbf, x = "batter", y = "count")
        for i, value in enumerate(mbf['count']):
            fig.add_annotation(
                x=mbf['batter'][i],
                y=value,
                text=str(value), showarrow=False, bgcolor="black")
        fig.update_layout(title = "Maximum balls faced by a batsman(Top 10)",title_x=0.35,title_y=1, width=900, height=400)
        st.plotly_chart(fig)

        st.markdown("****")

        death_runs, death_strike_rate = functions.destructive_batter(df1)
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<center><font size='4'><b>Batman runs in death overs (top 10)</b></font></center>", unsafe_allow_html=True)

            st.table(death_runs)
        with col2:
            st.markdown("<center><font size='4'><b>Strike  rate in death overs (top 10)</b></font></center>", unsafe_allow_html=True)

            st.table(death_strike_rate)

        st.markdown("****")

        st.markdown("<center><font size='5'><b>Bowling Average of Bowlers (top 10)</b></font></center>", unsafe_allow_html=True)

        runs_conc = df1.groupby(["bowler", "batsman_run"])["batsman_run"].sum().reset_index(allow_duplicates=True)
        runs_conc = runs_conc.loc[:, ~runs_conc.columns.duplicated(keep='last')]
        runs_conc = runs_conc.groupby("bowler")["batsman_run"].sum().sort_values().reset_index()
        runs_conc1 = runs_conc[runs_conc["batsman_run"]>1000].sort_values("batsman_run", ascending=False)

        total_wic1= df1[df1["isWicketDelivery"] == 1]["bowler"].value_counts().reset_index().sort_values("bowler", ascending=False)

        merged_df2 = pd.merge(runs_conc1, total_wic1, on='bowler', how='inner')
        merged_df2['Bowling Average'] = merged_df2['batsman_run'] / merged_df2['count']
        Bowling_Average = merged_df2[merged_df2["count"] >= 70].sort_values("Bowling Average", ascending=True).reset_index(drop=True)
        st.table(Bowling_Average.head(10))

        st.markdown("****")

        st.markdown("<center><font size='5'><b>Batting Average of Batsmen (top 10)</b></font></center>", unsafe_allow_html=True)

        b_run = df1[df1["batsman_run"] >= 1]
        out_delivery = df1[df1["isWicketDelivery"] == 1]
        result = b_run.groupby("batter")["batsman_run"].sum() >= 500
        filtered_batters = b_run.groupby("batter")["batsman_run"].sum()[result]
        batting_avg = ((filtered_batters.sort_values(ascending=False))/ (out_delivery["batter"].value_counts()).sort_values(
                ascending=False)).sort_values(ascending=False).head(10).reset_index()
        batting_avg.rename(columns = {"batter" : "batter", 0:"average"}, inplace=True)
        st.table(batting_avg)

        st.markdown("****")

        merge_df = df1.merge(df2, left_on="ID", right_on="ID")
        fig = px.pie(merge_df[merge_df["isWicketDelivery"] == 1], names="kind", width=1000, height=500)
        fig.update_layout(title="Type of Outs in IPL",title_x=0.5,width=700,height=400)
        st.plotly_chart(fig)

    expander3 = st.expander("See Explanation")
    with expander3:
        st.write("""Discover deeper insights within the "Player-Wise Analysis" section through two 
                 specialized tabs: "Analysis 1" and "Analysis 2." These tabs offer tailored avenues 
                 for users to explore diverse dimensions of player performance, statistics,
                   and trends within the IPL dataset. Whether examining batting averages,
                     bowling figures, or player contributions across seasons, each tab provides 
                     a focused platform to analyze and interpret player-centric data effectively.
                 Insights >>""")
        message = """* Orange Cap Holders
                    * Purple Cap Holders
                    * Most 6s by a Batsman in IPL (2008–2022)
                    * Top 10 Batsman by Runs
                    * Type of Dismissals in IPL
                    * Most 100s by a Batsman
                    * Most Catches By a Player
                    * Top 10 Wickets Takers in IPL
                    * Maximum Balls faced by a Batsman
                    * Batsman runs and strike rate in death overs
                    * Bowling Average of Bowlers (top 10)
                    * Batting Average of Batsmen (top 10)"""
        lines = message.split("\n")
        for i in lines:
            st.write(i)
    

if user_menu == "miscellaneous analysis":

    tab1, tab2, tab3 = st.tabs(["Analysis 1", "Analysis 2", "Analysis 3"])
    
    with tab1:

        umpire = functions.top_umpires(df1, df2)
        fig = px.pie(umpire, values='count', names='umpire_name', hole=.4, color_discrete_sequence=px.colors.sequential.Viridis)
        fig.update_traces(textinfo='value')
        fig.update_layout(title="Most matches as an umpire",title_x=0.5,width=700,height=400)
        st.plotly_chart(fig)

        st.markdown("****")

        total_fif = functions.top_10_fifities(df1, df2)
        fig = px.funnel(total_fif, x="batter", y='count')
        fig.update_xaxes(tickangle=45)
        fig.update_layout(title = "Most 50s by a Batsman 2008-2022",title_x=0.4,title_y=1, width=900, height=400)
        fig.update_traces(marker_color = "yellow", marker_line_color = 'black',marker_line_width = 2, opacity = 1)
        st.plotly_chart(fig)

        st.markdown("****")

        most_4 = functions.most_fours(df1)
        fig = px.scatter(most_4, x = "batter", y='count', size="count", size_max=60, color=most_4["count"])
        fig.update_xaxes(tickangle=45)
        for i, value in enumerate(most_4['count']):
            fig.add_annotation(
                x=most_4['batter'][i],
                y=value,
                text=str(value), showarrow=False, bgcolor="black")
        fig.update_layout(title = "Most 4s by a Batsman 2008-2022",title_x=0.4,title_y=1, width=900, height=400)
        fig.update_traces(marker_color = most_4["count"], marker_line_color = 'black',marker_line_width = 2, opacity = 1)
        st.plotly_chart(fig)


        st.markdown("****")

        five_wick = functions.five_wick(df1, df2)
        fig = px.funnel(five_wick, x ="bowler", y = "count")
        fig.update_xaxes(tickangle=45)
        fig.update_layout(title = "5 Wicket bowlers 2008-2022",title_x=0.4,title_y=1, width=900, height=400)
        fig.update_traces(marker_color = "brown", marker_line_color = 'black',marker_line_width = 2, opacity = 1)
        st.plotly_chart(fig)

        
    
    with tab2:
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)  
        with col1:
            sixes = df1[df1["batsman_run"] == 6]["batsman_run"].count()
            st.markdown("##### :green[Total 6s]")
            st.header(sixes)
        with col2:
            st.markdown("<div style='border-left: 2px solid #FFF; height: 100px;'></div>", unsafe_allow_html=True)
        
        
        with col3:
            fours = df1[df1["batsman_run"] == 4]["batsman_run"].count()
            st.markdown("##### :green[Total 4s]")
            st.header(fours)
        with col4:
            st.markdown("<div style='border-left: 2px solid #FFF; height: 100px;'></div>", unsafe_allow_html=True)

        with col5:
            merd_df = pd.merge(df1, df2, how='inner', on='ID')
            hunderds = merd_df.groupby(["ID", "batter"])["batsman_run"].sum().reset_index()
            hun_100 = hunderds[hunderds["batsman_run"] >= 100]["batsman_run"].count()
            st.markdown("##### :green[Total 100s]")
            st.header(hun_100)
        with col6:
            st.markdown("<div style='border-left: 2px solid #FFF; height: 100px;'></div>", unsafe_allow_html=True)

        with col7:
            merd_df = pd.merge(df1, df2, how='inner', on='ID')
            fift = merd_df.groupby(["ID", "batter"])["batsman_run"].sum().reset_index()
            hun_50 = fift[(fift["batsman_run"] >= 50) & (fift["batsman_run"] <100)]["batsman_run"].count()
            st.markdown("##### :green[Total 50s]")
            st.header(hun_50)

        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

        with col1:
            season = df2["Season"].nunique()
            st.markdown("##### :green[Seasons]")
            st.header(season)
        with col2:
            st.markdown("<div style='border-left: 2px solid #FFF; height: 100px;'></div>", unsafe_allow_html=True)

        with col3:
            b_run = df1[df1["batsman_run"] >= 1]
            top_10_bats = b_run.groupby("batter")["batsman_run"].sum().sum()
            st.markdown("##### :green[Runs]")
            st.header(top_10_bats)
        with col4:
            st.markdown("<div style='border-left: 2px solid #FFF; height: 100px;'></div>", unsafe_allow_html=True)

        with col5:
            total_balls = df1.shape[0]
            st.markdown("##### :green[Balls]")
            st.header(total_balls)
        with col6:
            st.markdown("<div style='border-left: 2px solid #FFF; height: 100px;'></div>", unsafe_allow_html=True)

        with col7:
            total_wick = df1[df1["isWicketDelivery"] == 1]["bowler"].value_counts().sum()
            st.markdown("##### :green[Wickets]")
            st.header(total_wick)


        st.markdown("****")
    
        most_3 = functions.most_threes(df1)
        fig = px.scatter(most_3, x = "batter", y='count', size="count", size_max=60, color=most_3["count"])
        fig.update_xaxes(tickangle=45)
        for i, value in enumerate(most_3['count']):
            fig.add_annotation(
                x=most_3['batter'][i],
                y=value,
                text=str(value), showarrow=False, bgcolor="black")
        fig.update_layout(title = "Most 3s by a Batsman 2008-2022",title_x=0.4,title_y=1, width=900, height=400)
        fig.update_traces(marker_color = "red", marker_line_color = 'black',marker_line_width = 2, opacity = 1)
        st.plotly_chart(fig)

        st.markdown("****")
        
        dots = functions.dot_balls(df1)
        fig = px.funnel(dots, y ="batter", x = "count")
        fig.update_xaxes(tickangle=45)
        fig.update_layout(title = "Most dot balls by a batsman 2008-2022",title_x=0.4,title_y=1, width=900, height=450)
        fig.update_traces(marker_color = "#2E8B57", marker_line_color = 'black',marker_line_width = 2, opacity = 1)
        st.plotly_chart(fig)


        st.markdown("****")
        st.markdown("<center><font size='6'><b>All Teams runs per over</b></font></center>", unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        mask = df1["batsman_run"] >=1
        six = df1[mask]
        pt = six.pivot_table(index="overs", columns="BattingTeam", values = "batsman_run", aggfunc="sum")
        fig, ax = plt.subplots(figsize=(20,20))
        ax = sns.heatmap(pt, annot=True, linewidth=.5, fmt='.5g')
        st.pyplot(fig)
        st.markdown("****")

        merd_df = pd.merge(df1, df2, how='inner', on='ID')
        total_10_scores = merd_df.groupby(["ID", "batter"])["batsman_run"].sum().reset_index()
        high_score = total_10_scores[["batter", "batsman_run"]]
        high_score = high_score.sort_values("batsman_run", ascending=False).reset_index().head(10)
        fig = px.scatter(high_score, x = "batter", y = "batsman_run", color="batter",size = "batsman_run", size_max=60)
        for i, value in enumerate(high_score['batsman_run']):
            fig.add_annotation(
                x=high_score['batter'][i],
                y=value,
                text=str(value), showarrow=False, bgcolor="black")
        fig.update_layout(title = "Top 10 Highest scorers in IPL",title_x=0.3,title_y=0.95, width=1000, height=500)
        st.plotly_chart(fig)

        

    with tab3:
        
        city_df = pd.read_csv("ipl_cities_lat_long.csv")
        import plotly.graph_objects as go

        col1, col2, col3 = st.columns([2,3,2])
        with col2:
            st.markdown("# :orange[IPL] Cities :green[Map]🗺️")
               

        city_coordinates = {
            'Ahmedabad': (23.0225, 72.5714),
            'Kolkata': (22.5726, 88.3639),
            'Mumbai': (19.0760, 72.8777),
            'Navi Mumbai': (19.0330, 73.0297),
            'Pune': (18.5204, 73.8567),
            'Dubai': (25.276987, 55.296249),
            'Sharjah': (25.3463, 55.4209),
            'Abu Dhabi': (24.4539, 54.3773),
            'Delhi': (28.7041, 77.1025),
            'Chennai': (13.0827, 80.2707),
            'Hyderabad': (17.3850, 78.4867),
            'Visakhapatnam': (17.6868, 83.2185),
            'Chandigarh': (30.7333, 76.7794),
            'Bengaluru': (12.9716, 77.5946),
            'Jaipur': (26.9124, 75.7873),
            'Indore': (22.7196, 75.8577),
            'Kanpur': (26.4499, 80.3319),
            'Rajkot': (22.3039, 70.8022),
            'Raipur': (21.2514, 81.6296),
            'Ranchi': (23.3441, 85.3096),
            'Cuttack': (20.4625, 85.8828),
            'Dharamsala': (32.2190, 76.3234),
            'Kochi': (9.9312, 76.2673),
            'Nagpur': (21.1458, 79.0882),
            'Johannesburg': (-26.2041, 28.0473),
            'Centurion': (-25.8603, 28.1894),
            'Durban': (-29.8587, 31.0218),
            'Bloemfontein': (-29.0852, 26.1596),
            'Port Elizabeth': (-33.9608, 25.6022),
            'Kimberley': (-28.7282, 24.7499),
            'East London': (-33.0292, 27.8546),
            'Cape Town': (-33.9249, 18.4241)
        }

        # Create lists for latitudes and longitudes
        lats = [lat for lat, lon in city_coordinates.values()]
        lons = [lon for lat, lon in city_coordinates.values()]
        city_names = list(city_coordinates.keys())

        fig = go.Figure(go.Scattermapbox(lat=lats,lon=lons,mode='markers',marker=go.scattermapbox.Marker(size=10
            , color = "red"),text=city_names))
        fig.update_layout(hovermode='closest',mapbox=dict(style='open-street-map',bearing=0,center=go.layout.mapbox.Center(
                    lat=sum(lats) / len(lats),
                    lon=sum(lons) / len(lons)),pitch=0,zoom=2),width = 930, height = 730)

        st.plotly_chart(fig)

        st.markdown("****")

        st.markdown("<center><font size='6'><b>All Teams sixes per over</b></font></center>", unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        mask = df1["batsman_run"] == 6
        six = df1[mask]
        pt = six.pivot_table(index="overs", columns="BattingTeam", values = "batsman_run", aggfunc="count")
        fig, ax = plt.subplots(figsize=(20,20))
        ax = sns.heatmap(pt, annot=True, linewidth=.5, fmt='.5g')
        st.pyplot(fig)

        st.markdown("****")

        extras = df1[["extra_type", "BattingTeam"]].value_counts().reset_index()
        fig = px.scatter(extras, x = "BattingTeam", y = "count", color="extra_type", symbol="extra_type", size_max=50)
        fig.update_layout(title = "Distribution of Extras by teams",title_x=0.3,title_y=0.95, width=1000, height=600)
        fig.update_traces(marker_line_color = 'black',marker_line_width = 2, opacity = 1, marker_size=15)
        st.plotly_chart(fig)

        st.markdown("****")

        batter_runs1 = df1[df1["batsman_run"] >= 1][["batter", "batsman_run"]].groupby("batter")["batsman_run"].sum()
        total_balls = df1["batter"].value_counts()
        strike_rate = ((batter_runs1/total_balls) * 100).reset_index()
        strike_rate.rename(columns={0:"strike_rate"}, inplace=True)
        batter_runs = df1[df1["batsman_run"] >= 1][["batter", "batsman_run"]].groupby("batter")["batsman_run"].sum().reset_index()
        result_df = pd.merge(strike_rate, batter_runs, on="batter")
        strike_run = result_df[["batter", "strike_rate", "batsman_run"]]
        strike_run.sort_values("batsman_run", ascending=False)
        fig, ax = plt.subplots(figsize=(12,5))
        ax = sns.scatterplot(data = strike_run, x="batsman_run", y="strike_rate")
        plt.title("Batsman runs vs Strike rate")
        st.pyplot(fig)

        st.markdown("****")
        merd_df = pd.merge(df1, df2, how='inner', on='ID')
        total_10_scores = merd_df.groupby(["ID", "batter"])["batsman_run"].sum().reset_index()
        high_score = total_10_scores[["batter", "batsman_run"]]
        high_score = high_score.sort_values("batsman_run", ascending=False).reset_index().head(10)
        fig = px.scatter(high_score, x = "batter", y = "batsman_run", color="batter", size_max=50)
        fig.update_layout(title = "Top 10 Highest scorers in IPL",title_x=0.3,title_y=0.95, width=1000, height=600)
        fig.update_traces(marker_line_color = 'black',marker_line_width = 2, opacity = 1, marker_size=15)
        st.plotly_chart(fig)

    expander4 = st.expander("See Explanation")
    with expander4:
        st.write("""In the "Miscellaneous Analysis" section, we delve into various aspects of IPL 
                 data through three tabs: Analysis 1, 2, and 3. Here, we explore intriguing insights 
                 such as IPL's global impact, visualized through maps showcasing its influence beyond
                   the country's borders. Additionally, we utilize heatmaps and donut charts to uncover
                     patterns and trends within the IPL dataset, offering a comprehensive exploration of 
                     diverse facets of cricket's premier T20 league.""")
        message = """
                * Most Matches as an IPL Umpire
                * All Teams' Runs per over Using HeatMap
                * Distribution of Extras By IPL Teams
                * Simple Stats Dashboard
                * Most 50s by a Batsman (2008–2022). 
                * Most 4s by a Batsman
                * 5 Wicket Bowlers
                * Most 3s by a Batsman
                * Most Dot balls by a Batsman
                * Top 10 Highest Scorers in IPL
                * All Teams Sixes per over
                * Batsman runs vs Strike Rate
                * All IPL cities where IPL Held using Map
                """
        lines = message.split("\n")
        for i in lines:
            st.write(i)
