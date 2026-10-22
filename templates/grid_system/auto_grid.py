from collections import defaultdict
from dash import html, dcc
import dash_bootstrap_components as dbc


class AutoGrid:

    def __init__(
        self,
        items,
        container_height="100vh",
        gap="8px"
    ):

        self.items = dict(sorted(items.items()))

        self.container_height = container_height
        self.gap = gap

        self.validate()


    def validate(self):

        row_widths = defaultdict(dict)
        stack_heights = defaultdict(int)

        for grid_id, config in self.items.items():

            if len(grid_id) != 3:
                raise ValueError(
                    f"{grid_id} must contain exactly 3 chars"
                )

            required = [
                "fig",
                "width",
                "height"
            ]

            for key in required:

                if key not in config:

                    raise ValueError(
                        f"{grid_id} missing '{key}'"
                    )

            # parse ids
            row_id = grid_id[0]
            col_id = grid_id[1]

            row_key = row_id
            col_key = row_id + col_id
      
            # width validation
            if col_id not in row_widths[row_key]:

                row_widths[row_key][col_id] = config["width"]

            else:

                existing = row_widths[row_key][col_id]

                if existing != config["width"]:

                    raise ValueError(
                        f"{grid_id} width mismatch inside column"
                    )

            # height validation
            stack_heights[col_key] += config["height"]

        # validate row widths
        for row_key, cols in row_widths.items():

            total = sum(cols.values())

            if total != 100:

                raise ValueError(
                    f"Row '{row_key}' width total = {total}, must be 100"
                )

        # validate stack heights
        for col_key, total in stack_heights.items():

            if total != 100:

                raise ValueError(
                    f"Column '{col_key}' height total = {total}, must be 100"
                )

    def build(self):

        rows = defaultdict(lambda: defaultdict(list))

        # build hierarchy
        for grid_id, config in self.items.items():

            row_id = grid_id[0]
            col_id = grid_id[1]

            rows[row_id][col_id].append(
                (grid_id, config)
            )

        # build rows
        row_components = []

        for row_id in sorted(rows.keys()):

            cols = rows[row_id]

            col_components = []

            column_sizes = []

            # build columns
            for col_id in sorted(cols.keys()):

                stack_items = cols[col_id]

                # width
                width = stack_items[0][1]["width"]

                column_sizes.append(f"{width}fr")

                # stack rows
                stack_template = []

                children = []

                for grid_id, config in stack_items:

                    height = config["height"]

                    stack_template.append(
                        f"{height}fr"
                    )

                    children.append(

                        dbc.Card(
                            dbc.CardBody([
                                html.H2(
                                    config["title"],
                                    className="chart-card-title"
                                ),
                                html.Div(
                                    dcc.Graph(
                                        figure=config["fig"],
                                        className="chart-figure"
                                    ), 
                                    className="chart-card-container"
                                )
                            ]),
                            className="chart-card"
                        )
                    )

                # column container
                col_components.append(

                    html.Div(

                        children,

                        style={

                            "display": "grid",

                            "gridTemplateRows":
                                " ".join(stack_template),

                            "gap": self.gap,

                            "height": "100%"
                        }

                    )

                )

            # row container
            row_components.append(

                html.Div(

                    col_components,

                    style={

                        "display": "grid",

                        "gridTemplateColumns":
                            " ".join(column_sizes),

                        "gap": self.gap,

                        "height": "100%"
                    }

                )

            )

        # root container
        return html.Div(

            row_components,

            style={

                "display": "grid",

                "gridTemplateRows": f"repeat({len(row_components)}, 1fr)",

                "gap": self.gap,

                "height": self.container_height,

            },

            className="grid_container"

        )
