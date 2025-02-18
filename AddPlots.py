import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

class Plots:
    def __init__(self, data: pd.DataFrame):
        self.data = data
    
    def display(self):
        tab1, tab2, tab3 = st.tabs(["Perform Operations", "View Operations", "Clear Memory"])
        
        with tab1:
            st.subheader("Configure Plot Parameters")
            
            # Select columns
            columns = st.multiselect("Select columns to plot", self.data.columns.tolist())
            
            # Select kind of plot
            kind = st.selectbox("Select plot type", ["line", "bar", "barh", "hist", "box", "kde", "density", "area", "pie", "scatter", "hexbin"], index=0)
            
            # Other parameters
            subplots = st.checkbox("Subplots", value=False)
            sharex = st.checkbox("Share X-axis", value=True)
            sharey = st.checkbox("Share Y-axis", value=False)
            layout = st.text_input("Layout (rows, cols)", "")
            figsize = st.text_input("Figure Size (width, height)", "")
            use_index = st.checkbox("Use Index", value=True)
            title = st.text_input("Title", "")
            grid = st.checkbox("Grid", value=False)
            legend = st.checkbox("Legend", value=True)
            logx = st.checkbox("Log X-axis", value=False)
            logy = st.checkbox("Log Y-axis", value=False)
            loglog = st.checkbox("Log Both Axes", value=False)
            xlabel = st.text_input("X-axis Label", "")
            ylabel = st.text_input("Y-axis Label", "")
            rot = st.number_input("Rotation", value=0)
            fontsize = st.number_input("Font Size", value=12)
            colormap = st.text_input("Colormap", "")
            colorbar = st.checkbox("Colorbar (only for scatter/hexbin)", value=False)
            stacked = st.checkbox("Stacked (for bar/area)", value=False)
            secondary_y = st.checkbox("Secondary Y-axis", value=False)
            mark_right = st.checkbox("Mark Right Axis", value=True)
            
            col1, col2 = st.columns([1, 3])
            with col1:
                plot_button = st.button("Plot")
                
            with col2:
                if plot_button and columns:
                    fig, ax = plt.subplots(figsize=eval(figsize) if figsize else (8, 6))
                    self.data[columns].plot(
                        kind=kind,
                        subplots=subplots,
                        sharex=sharex,
                        sharey=sharey,
                        layout=eval(layout) if layout else None,
                        figsize=eval(figsize) if figsize else None,
                        use_index=use_index,
                        title=title,
                        grid=grid,
                        legend=legend,
                        logx=logx,
                        logy=logy,
                        loglog=loglog,
                        xlabel=xlabel,
                        ylabel=ylabel,
                        rot=rot,
                        fontsize=fontsize,
                        colormap=colormap if colormap else None,
                        colorbar=colorbar if kind in ["scatter", "hexbin"] else False,
                        stacked=stacked,
                        secondary_y=secondary_y,
                        mark_right=mark_right,
                        ax=ax
                    )
                    st.pyplot(fig)
        
        with tab2:
            st.subheader("View Operations")
            st.write("Feature under development.")
        
        with tab3:
            st.subheader("Clear Memory")
            if st.button("Clear DataFrame from Memory"):
                self.data = pd.DataFrame()
                st.success("Data cleared!")
