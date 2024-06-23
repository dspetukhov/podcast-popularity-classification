import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly import io
io.renderers.default = 'plotly_mimetype+notebook'


def get_figure(stats):
    figure = go.FigureWidget(
        make_subplots(rows=1, cols=2, shared_xaxes=True),
    )
    #
    figure.add_trace(
        go.Scatter(
            x=stats['epoch'],
            y=stats['training_loss'],
            mode='lines+markers',
            marker=_get_marker_dict(),
            line=_get_line_dict(),
            name='Training'
        ),
        row=1, col=1
    )
    figure.add_trace(
        go.Scatter(
            x=stats['epoch'],
            y=stats['testing_loss'],
            mode='lines+markers',
            marker=_get_marker_dict(False),
            line=_get_line_dict(False),
            name='Testing'
        ),
        row=1, col=1
    )
    #
    figure.add_trace(
        go.Scatter(
            x=stats['epoch'],
            y=stats['training_auc'],
            mode='lines+markers',
            marker=_get_marker_dict(),
            line=_get_line_dict(),
            showlegend=False
        ),
        row=1, col=2
    )
    figure.add_trace(
        go.Scatter(
            x=stats['epoch'],
            y=stats['testing_auc'],
            mode='lines+markers',
            marker=_get_marker_dict(False),
            line=_get_line_dict(False),
            showlegend=False
        ),
        row=1, col=2
    )
    #
    figure.update_layout(plot_bgcolor = 'white', width=1100, height=500, font_family='Arial', font_size=12)
    figure.update_xaxes(title_text='Epoch')
    figure.update_yaxes(title_text='Loss', row=1, col=1)
    figure.update_yaxes(title_text='AUC ROC', row=1, col=2)
    figure.update_xaxes(showgrid=True, gridwidth=0.1, gridcolor='lightgrey', griddash='dot', showline=True, linecolor='black', mirror=True)
    figure.update_yaxes(showgrid=True, gridwidth=0.1, gridcolor='lightgrey', griddash='dot', showline=True, linecolor='black', mirror=True)
    #
    return figure


def update_figure(figure, stats, filename):
    for idx, key in enumerate(stats):
        if idx:
            scatter = figure.data[idx-1]
            scatter.x = stats['epoch']
            scatter.y = stats[key]
    figure.write_image(f'artifacts/{filename}.png')
    # figure.write_html(f'artifacts/{filename}.html')
    return


def _get_marker_dict(training=True):
    return dict(
        color='white',
        size=6,
        line=dict(
            color='black' if training else 'red',
            width=1
        )
    )

def _get_line_dict(training=True):
    return dict(
        color='black' if training else 'red',
        width=0.5,
        dash='dash'
    )