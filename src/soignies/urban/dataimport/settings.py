# -*- coding: utf-8 -*-

from imio.urban.dataimport.browser.controlpanel import ImporterControlPanel
from imio.urban.dataimport.browser.import_panel import ImporterSettings
from imio.urban.dataimport.browser.import_panel import ImporterSettingsForm
from imio.urban.dataimport.urbaweb.settings import UrbawebImporterFromImportSettings


class SoigniesImporterSettingsForm(ImporterSettingsForm):
    """ """

class SoigniesImporterSettings(ImporterSettings):
    """ """
    form = SoigniesImporterSettingsForm


class SoigniesImporterControlPanel(ImporterControlPanel):
    """ """
    import_form = SoigniesImporterSettings


class SoigniesImporterFromImportSettings(UrbawebImporterFromImportSettings):
    """ """

    def get_importer_settings(self):
        """
        Return the db name to read.
        """
        settings = super(SoigniesImporterFromImportSettings, self).get_importer_settings()

        db_settings = {
            'db_name': '',
        }

        settings.update(db_settings)

        return settings
