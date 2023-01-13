import streamlit as st
import streamlit.components.v1 as components

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

# Space out the maps so the first one is 2x the size of the other three
c1, c2, c3, = st.columns((1, 1, 1))

html_temp = "<div class='tableauPlaceholder' id='viz1673599584494' style='position: relative'><noscript><a href='#'><img alt='Real Eastate Dashboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Re&#47;RealEstateDashboard_16735995671000&#47;RealEastateDashboard&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='RealEstateDashboard_16735995671000&#47;RealEastateDashboard' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Re&#47;RealEstateDashboard_16735995671000&#47;RealEastateDashboard&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='fr-FR' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1673599584494');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1280px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1280px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='1177px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
components.html(html_temp, width = 1280, height = 800)

