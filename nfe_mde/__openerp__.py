# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2015  Danimar Ribeiro www.trustcode.com.br                    #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU Affero General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU Affero General Public License for more details.                         #
#                                                                             #
# You should have received a copy of the GNU Affero General Public License    #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
###############################################################################

{
    'name': 'Manifesto Destinatário NFe',
    'version': '8.0.1.0.0',
    'category': 'NFE',
    'author': 'Danimar Ribeiro',
    'license': 'AGPL-3',
    'website': 'http://www.trustcode.com.br',
    'description': """
        Implementa a consulta de nfe periodicamente no SEFAZ
      Este módulo serve para efetuar download de notas em que são destinada
      a empresa.
      Manifesta a ciência ou desconhecimento da NF-e

      Dependencias: pysped, geraldo, pyxmlsec
      Instalando pyxmlsec
        sudo pip install pyxmlsec
        Dependencias ->
        sudo apt-get install libxmlsec1-dev
        sudo apt-get install libxml2-dev
      Instalando geraldo
        sudo pip install geraldo
    """,
    'depends': [
        'nfe',
        'nfe_attach',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/nfe_schedule.xml',
        'views/nfe_mde_view.xml'
    ],
    'installable': True,
    'active': False,
}
