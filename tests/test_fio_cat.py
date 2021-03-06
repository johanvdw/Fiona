import json

import click
from click.testing import CliRunner

from fiona.fio import cat


input = u'\x1e{"geometry": {"coordinates": [[[100094.81257811641, 6684726.008762141], [98548.69617048775, 6684924.5976624405], [87664.09899970173, 6686905.046363058], [86952.87877302397, 6687103.688267614], [85283.08641112497, 6688045.252446961], [84540.91936600611, 6688936.450241844], [82963.96745943041, 6691364.418923092], [82469.15232285221, 6692405.682380612], [81819.82573305666, 6693843.436658373], [82438.31682390235, 6697660.772804541], [83365.94214068248, 6700140.454427341], [84633.75982132941, 6700339.2401707815], [88066.07368095664, 6699495.907563213], [99321.69871455646, 6696173.432660581], [100651.41003208276, 6695726.6230187025], [101177.06066760799, 6695379.438652324], [103588.9087551346, 6692158.022348123], [104269.2934828625, 6691215.983683517], [105073.24284537231, 6689679.516414698], [105475.21752662722, 6688540.508853204], [105506.16434506832, 6687846.5876325965], [105413.32388974504, 6687203.011032262], [104918.6200726609, 6686856.189040878], [100713.19234947088, 6684875.573921225], [100094.81257811641, 6684726.008762141]]], "type": "Polygon"}, "id": "0", "properties": {"AREA": 244820.0, "CAT": 232.0, "CNTRY_NAME": "United Kingdom", "FIPS_CNTRY": "UK", "POP_CNTRY": 60270708.0}, "type": "Feature"}\n'

input_collection = u'\x1e{"features": [{"geometry": {"coordinates": [[[100094.81257811641, 6684726.008762141], [98548.69617048775, 6684924.5976624405], [87664.09899970173, 6686905.046363058], [86952.87877302397, 6687103.688267614], [85283.08641112497, 6688045.252446961], [84540.91936600611, 6688936.450241844], [82963.96745943041, 6691364.418923092], [82469.15232285221, 6692405.682380612], [81819.82573305666, 6693843.436658373], [82438.31682390235, 6697660.772804541], [83365.94214068248, 6700140.454427341], [84633.75982132941, 6700339.2401707815], [88066.07368095664, 6699495.907563213], [99321.69871455646, 6696173.432660581], [100651.41003208276, 6695726.6230187025], [101177.06066760799, 6695379.438652324], [103588.9087551346, 6692158.022348123], [104269.2934828625, 6691215.983683517], [105073.24284537231, 6689679.516414698], [105475.21752662722, 6688540.508853204], [105506.16434506832, 6687846.5876325965], [105413.32388974504, 6687203.011032262], [104918.6200726609, 6686856.189040878], [100713.19234947088, 6684875.573921225], [100094.81257811641, 6684726.008762141]]], "type": "Polygon"}, "id": "0", "properties": {"AREA": 244820.0, "CAT": 232.0, "CNTRY_NAME": "United Kingdom", "FIPS_CNTRY": "UK", "POP_CNTRY": 60270708.0}, "type": "Feature"}], "type": "FeatureCollection" }\n'


def test_cat():
    runner = CliRunner()
    result = runner.invoke(
        cat.cat,
        ['docs/data/test_uk.shp'],
        catch_exceptions=False)
    assert result.exit_code == 0
    assert result.output.count('"Feature"') == 48


def test_cat_bbox_no():
    runner = CliRunner()
    result = runner.invoke(
        cat.cat,
        ['docs/data/test_uk.shp', '--bbox', '-90,10,-80,20'],
        catch_exceptions=False)
    assert result.exit_code == 0
    assert result.output == ""


def test_cat_bbox_yes():
    runner = CliRunner()
    result = runner.invoke(
        cat.cat,
        ['docs/data/test_uk.shp', '--bbox', '-10,50,0,60'],
        catch_exceptions=False)
    assert result.exit_code == 0
    assert result.output.count('"Feature"') == 44


def test_collect_rs():
    runner = CliRunner()
    result = runner.invoke(
        cat.collect,
        ['--src_crs', 'EPSG:3857'],
        input,
        catch_exceptions=False)
    assert result.exit_code == 0
    assert result.output == u'{"features": [{"geometry": {"coordinates": [[[0.8991670000000086, 51.357216], [0.8852780000000007, 51.358329999999995], [0.7874999999999889, 51.369438], [0.7811109999999931, 51.37055199999999], [0.766110999999994, 51.375831999999996], [0.7594439999999931, 51.380828999999984], [0.7452780000000093, 51.39443999999999], [0.7408329999999906, 51.40027599999999], [0.735000000000005, 51.408332999999985], [0.7405559999999894, 51.42971799999999], [0.7488889999999875, 51.44360399999998], [0.7602780000000084, 51.444717], [0.7911109999999926, 51.439994999999996], [0.8922220000000026, 51.42138700000001], [0.9041670000000085, 51.418884000000006], [0.9088890000000031, 51.416938999999985], [0.9305549999999989, 51.39888799999999], [0.9366669999999937, 51.393608000000015], [0.9438890000000006, 51.38499499999999], [0.9475000000000044, 51.37860899999998], [0.9477780000000093, 51.374717999999994], [0.9469439999999942, 51.37110899999997], [0.9425000000000048, 51.36916399999999], [0.904721999999989, 51.358054999999986], [0.8991670000000086, 51.357216]]], "type": "Polygon"}, "id": "0", "properties": {"AREA": 244820.0, "CAT": 232.0, "CNTRY_NAME": "United Kingdom", "FIPS_CNTRY": "UK", "POP_CNTRY": 60270708.0}, "type": "Feature"}], "type": "FeatureCollection"}\n'


def test_collect_no_rs():
    runner = CliRunner()
    result = runner.invoke(
        cat.collect,
        ['--src_crs', 'EPSG:3857'],
        input,
        catch_exceptions=False)
    assert result.exit_code == 0
    assert result.output == u'{"features": [{"geometry": {"coordinates": [[[0.8991670000000086, 51.357216], [0.8852780000000007, 51.358329999999995], [0.7874999999999889, 51.369438], [0.7811109999999931, 51.37055199999999], [0.766110999999994, 51.375831999999996], [0.7594439999999931, 51.380828999999984], [0.7452780000000093, 51.39443999999999], [0.7408329999999906, 51.40027599999999], [0.735000000000005, 51.408332999999985], [0.7405559999999894, 51.42971799999999], [0.7488889999999875, 51.44360399999998], [0.7602780000000084, 51.444717], [0.7911109999999926, 51.439994999999996], [0.8922220000000026, 51.42138700000001], [0.9041670000000085, 51.418884000000006], [0.9088890000000031, 51.416938999999985], [0.9305549999999989, 51.39888799999999], [0.9366669999999937, 51.393608000000015], [0.9438890000000006, 51.38499499999999], [0.9475000000000044, 51.37860899999998], [0.9477780000000093, 51.374717999999994], [0.9469439999999942, 51.37110899999997], [0.9425000000000048, 51.36916399999999], [0.904721999999989, 51.358054999999986], [0.8991670000000086, 51.357216]]], "type": "Polygon"}, "id": "0", "properties": {"AREA": 244820.0, "CAT": 232.0, "CNTRY_NAME": "United Kingdom", "FIPS_CNTRY": "UK", "POP_CNTRY": 60270708.0}, "type": "Feature"}], "type": "FeatureCollection"}\n'


def test_collect_ld():
    runner = CliRunner()
    result = runner.invoke(
        cat.collect,
        ['--with-ld-context', '--add-ld-context-item', 'foo=bar'],
        input,
        catch_exceptions=False)
    assert result.exit_code == 0
    assert '"@context": {' in result.output
    assert '"foo": "bar"' in result.output


def test_collect_rec_buffered():
    runner = CliRunner()
    result = runner.invoke(cat.collect, ['--record-buffered'], input)
    assert result.exit_code == 0
    assert '"FeatureCollection"' in result.output


def test_distrib():
    runner = CliRunner()
    result = runner.invoke(cat.distrib, [], input)
    assert result.exit_code == 0
    assert json.loads(result.output.strip())['id'] == '0'



def test_distrib():
    runner = CliRunner()
    result = runner.invoke(cat.distrib, [], input_collection)
    assert result.exit_code == 0
    assert json.loads(result.output.strip())['parent'] == 'collection:0'
    assert json.loads(result.output.strip())['id'] == '0'


def test_dump():
    runner = CliRunner()
    result = runner.invoke(cat.dump, ['docs/data/test_uk.shp'])
    assert result.exit_code == 0
    assert '"FeatureCollection"' in result.output
