
import os.path as osp

from .notebook_utils import NotebookUtilities
nu = NotebookUtilities(
    data_folder_path=osp.abspath('../data'),
    saves_folder_path=osp.abspath('../saves')
)

from .choropleth_utils import ChoroplethUtilities
us_stats_df = nu.load_object('us_stats_df')
all_countries_df = nu.load_object('all_countries_df')
cu = ChoroplethUtilities(
    iso_3166_2_code='us',
    one_country_df=us_stats_df,
    all_countries_df=all_countries_df
)

from .stats_charting_utils import StatsChartingUtilities
scu = StatsChartingUtilities()

from .stats_scraping_utils import StatsScrapingUtilities
ssu = StatsScrapingUtilities()