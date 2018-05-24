# -*- coding: utf-8 -*-
# @Author: Abhi
# @Date:   2018-05-22 21:06:26
# @Last Modified by:   Abhi
# @Last Modified time: 2018-05-22 22:00:40

import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

plotly.tools.set_credentials_file(username="navravi", api_key="uYbUJOZ3VYmK0YILm3Gq")

N = 500

trace_caucasian = go.Scatter(
    x = np.random.randn(N),
    y = np.random.randn(N)+2,
    name = 'Caucasian',
    mode = 'markers',
    marker = dict(
        size = 10,
        color = 'rgba(39, 174, 96,1.0)',
        line = dict(
            width = 2,
            color = 'rgb(0, 0, 0)'
        )
    )
)

trace_african_american = go.Scatter(
    x = np.random.randn(N),
    y = np.random.randn(N)-2,
    name = 'African-American',
    mode = 'markers',
    marker = dict(
        size = 10,
        color = 'rgba(41, 128, 185,1.0)',
        line = dict(
            width = 2,
        )
    )
)

trace_hispanic = go.Scatter(
    x = np.random.randn(N),
    y = np.random.randn(N)+2,
    name = 'Hispanic',
    mode = 'markers',
    marker = dict(
        size = 10,
        color = 'rgba(142, 68, 173,1.0)',
        line = dict(
            width = 2,
            color = 'rgb(0, 0, 0)'
        )
    )
)

trace_native_american = go.Scatter(
    x = np.random.randn(N),
    y = np.random.randn(N)-2,
    name = 'Native American',
    mode = 'markers',
    marker = dict(
        size = 10,
        color = 'rgba(230, 126, 34,1.0)',
        line = dict(
            width = 2,
        )
    )
)

trace_asian = go.Scatter(
    x = np.random.randn(N),
    y = np.random.randn(N)+2,
    name = 'Asian',
    mode = 'lines+markers',
    marker = dict(
        size = 10,
        color = 'rgba(231, 76, 60,1.0)',
        line = dict(
            width = 2,
            color = 'rgb(0, 0, 0)'
        )
    )
)

trace_other = go.Scatter(
    x = np.random.randn(N),
    y = np.random.randn(N)-2,
    name = 'Other',
    mode = 'markers',
    marker = dict(
        size = 10,
        color = 'rgba(52, 73, 94,1.0)',
        line = dict(
            width = 2,
        )
    )
)

data = [trace_caucasian, trace_african_american, trace_hispanic, trace_native_american, trace_asian, trace_other]

layout = dict(title = 'Styled Scatter',
              yaxis = dict(zeroline = False),
              xaxis = dict(zeroline = False)
             )

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='styled-scatter')
