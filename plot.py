import seaborn as sns
import matplotlib as mpl
import pandas as pd
import matplotlib.pyplot as plt

sns.set_theme(style="darkgrid")

class plotfuncs():

  def __init__(self):
    self.x_data = "s"
    self.y_data = "k"
    self.rating = "r"
    self.level = "level"
    self.action = "action"

  def listfuncs(self):
    print("""
      lmplot scatterplot lineplot
      histplot boxplot jointgrid
      displot relplot lmplotAllInOne
    """)

  def lmplot(self,data):
    sns.lmplot(
        data=data, x=self.x_data, y=self.y_data, 
        col=self.action, hue=self.level,
        col_wrap=2, palette="muted", ci=None,
        height=4, scatter_kws={"s": 50, "alpha": 1}
    )

  def scatterplot(self,data,xsize,ysize):
    f, ax = plt.subplots(figsize=(xsize, ysize))
    sns.despine(f, left=True, bottom=True)
    clarity_ranking = data[self.level].unique()
    sns.scatterplot(x=self.x_data, y=self.y_data,
                    hue=self.level, size=self.action,
                    palette="ch:r=-.2,d=.3_r",
                    hue_order=clarity_ranking,
                    sizes=(1, 8), linewidth=0,
                    data=stackedRow, ax=ax)
    
  def lineplot(self,data,xsize,ysize):
    f, ax = plt.subplots(figsize=(xsize, ysize))
    sns.lineplot(x=self.x_data, y=self.y_data,
                hue=self.level, style=self.action,
                data=data)
    
  def histplot(self,data,xsize,ysize,start,end,step):
    f, ax = plt.subplots(figsize=(xsize, ysize))
    sns.despine(f)
    sns.histplot(
        data,
        x=self.rating, hue=self.level,
        multiple="stack",
        palette="light:m_r",
        edgecolor=".3",
        linewidth=.5,
        log_scale=True,
    )
    ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
    ax.set_xticks(np.arange(start,end,step))

  def boxplot(self,data,xsize,ysize):
    f, ax = plt.subplots(figsize=(xsize, ysize))
    ax.set_xscale("log")
    sns.boxplot(x=self.rating, y=self.level, data=data,
                whis=[0, 100], width=.6, palette="vlag")

    sns.stripplot(x=self.rating, y=self.level, data=data,
                  size=4, color=".3", linewidth=0)

    ax.xaxis.grid(True)
    ax.set(ylabel="")
    sns.despine(trim=True, left=True)

  def jointgrid(self,data,xsize,ysize):
    f, ax = plt.subplots(figsize=(xsize, ysize))
    g = sns.JointGrid(data=data, x=self.x_data, y=self.y_data,hue=self.level, space=0, ratio=17)
    g.plot_joint(sns.scatterplot, size=data["r"], sizes=(30, 120),
                color="g", alpha=.6, legend=False)
    g.plot_marginals(sns.rugplot, height=1, color="g", alpha=.6)

  def displot(self,data,xsize,ysize):
    f, ax = plt.subplots(figsize=(xsize, ysize))
    sns.displot(
      data=data,
      x=self.rating, hue=self.level,
      kind="kde", height=6,
      multiple="fill", clip=(0, None),
      palette="ch:rot=-.25,hue=1,light=.75",
    )

  def relplot(self,data,xsize,ysize):
    f, ax = plt.subplots(figsize=(xsize, ysize))
    sns.relplot(x=self.x_data, y=self.y_data, hue=self.level, size=self.action,
            sizes=(40, 400), alpha=.5, palette="muted",
            height=6, data=data)
    
  def lmplotAllinOne(self,data,xsize,ysize):
    f, ax = plt.subplots(figsize=(xsize, ysize))
    g = sns.lmplot(
      data=data,
      x=self.x_data, y=self.y_data, hue=self.level,
      height=5
    )

plotfunctions = plotfuncs()
