import time
import numpy as np
import streamlit as st
from PIL import Image
st.title('Local dishes of Nagano Prefecture ')
st.title('長野県の郷土料理')
st.write('Nagano Prefecture, extending longitudinally from north to south, boasts a variety of Local dishes that differ across its diverse geographical areas. ')
st.write('長野県は南北に長く地域によってさまざまな郷土料理があります')
# text = st.text_input('あなたの名前を教えてください。')
# st.write('あなたの名前は'+text+'です')
# condition = st.slider('あなたの今の調子は?',0, 100, 50)
#option = st.selectbox(
#'郷土料理について知りたい地域を選択してください',
#list(['北信','東信','南信','中信'])

import streamlit as st
options = ['Hokushin北信', 'Tyuushin中信', 'Nansin南信','Toushin東信',
           'All regions全域']

# selectboxを作成
selected_option = st.selectbox('Please select the region for which you would like to learn about local dishes. 郷土料理について知りたい地域を選択してください', options)

# 選択されたオプションに基づいて情報を表示
if selected_option == 'Hokushin北信':
    st.write('北信：ego,nasusenbei,sasasusi,えご,なす煎餅,笹ずし ')
    from PIL import Image
    img = Image.open('8254_1.jpg')
    st.image(img,caption='nasusenbei,なす煎餅',use_column_width=True)
    import pandas as pd
    import numpy as np

    from PIL import Image
    img = Image.open('nagano_20_1.jpg')
    st.image(img,caption='ego,えご',use_column_width=True)
    import pandas as pd
    import numpy as np

    from PIL import Image
    img = Image.open('nagano_7_1.jpg')
    st.image(img,caption='sasasusi,笹ずし',use_column_width=True)
    import pandas as pd
    import numpy as np

    from PIL import Image
    img = Image.open('001a.gif')
    st.image(img,caption='Nagano,長野県',use_column_width=True)
    import pandas as pd
    import numpy as np

    #df = pd.DataFrame(
    #np.random.rand(100,2)/[50,50] + [35.69,139.70],
    #columns = ['lat','lon',]#lat lon 緯度と経度
    #)
    ##緯度と経度から地図に書き込む
    #st.map(df)
elif selected_option == 'Tyuushin中信':
    st.write('中信：ego,sanzokuyakiえご,山賊焼')
    import pandas as pd
    import numpy as np

    from PIL import Image
    img = Image.open('nagano_20_1.jpg')
    st.image(img,caption='ego,えご',use_column_width=True)
    import pandas as pd
    import numpy as np

    from PIL import Image
    img = Image.open('spe2_02_07.jpg')
    st.image(img,caption='sanzokuyaki,山賊焼',use_column_width=True)
    import pandas as pd
    import numpy as np

    from PIL import Image
    img = Image.open('001a.gif')
    st.image(img,caption='Nagano,長野県',use_column_width=True)
    import pandas as pd
    import numpy as np

    #df = pd.DataFrame(
    #np.random.rand(100,2)/[50,50] + [35.69,139.70],
    #columns = ['lat','lon',]#lat lon 緯度と経度
    #)
    #緯度と経度から地図に書き込む
    #st.map(df)
elif selected_option == 'Nansin南信':
    st.write('南信：shunkiすんき')
    import pandas as pd
    import numpy as np

    from PIL import Image
    img = Image.open('nagano_1_1.jpg')
    st.image(img,caption='shunkiすんき',use_column_width=True)
    import pandas as pd
    import numpy as np

    from PIL import Image
    img = Image.open('001a.gif')
    st.image(img,caption='Nagano,長野県',use_column_width=True)
    import pandas as pd
    import numpy as np
    

   # df = pd.DataFrame(
    #np.random.rand(100,2)/[50,50] + [35.69,139.70],
    #columns = ['lat','lon',]#lat lon 緯度と経度
    #)
    #緯度と経度から地図に書き込む
    #st.map(df)
elif selected_option == 'Toushin東信':
    st.write('koikoku,鯉こく')
    import pandas as pd
    import numpy as np

    from PIL import Image
    img = Image.open('nagano_11_1.jpg')
    st.image(img,caption='koikoku,鯉こく',use_column_width=True)
    import pandas as pd
    import numpy as np

    from PIL import Image
    img = Image.open('001a.gif')
    st.image(img,caption='Nagano,長野県',use_column_width=True)
    import pandas as pd
    import numpy as np

elif selected_option == 'All regions全域':
    st.write('全域：shiomaruika,しおまるいか')
    import pandas as pd
    import numpy as np

    from PIL import Image
    img = Image.open('spe2_02_07.jpg')
    st.image(img,caption='shiomaruikaしおまるいか',use_column_width=True)
    import pandas as pd
    import numpy as np

    from PIL import Image
    img = Image.open('001a.gif')
    st.image(img,caption='Nagano,長野県',use_column_width=True)
    import pandas as pd
    import numpy as np

    df = pd.DataFrame(
    columns = ['38.55','135.33',]#lat lon 緯度と経度
    )
    #緯度と経度から地図に書き込む
    st.map(df)


# st.sidebar.write('プログレスバーの表示')
# 'Start!'

# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#     latest_iteration.text(f'Iteration{i+1}')
#     bar.progress(i +1)
#     time.sleep(0.1)

#'Done!!!'
#button = left_column.button('右カラムに文字を表示')
#if button:
# right_column.write('ここは右カラムです')

#from PIL import Image
#img = Image.open('S__83451917_0.jpg')
#st.image(img,caption='紙',use_column_width=True)


#import pandas as pd
#df = pd.DataFrame(
#   np.random.rand(100,2)/[50,50] + [35.69,139.70],
#    columns = ['lat','lon',]#lat lon 緯度と経度
#)
#st.map(df)

# import numpy as np
#df = pd.DataFrame(
    #np.random.rand(20,3), #20行3列
    #columns = ['a','b','c']
#st.table(df.style.highlight_max(axis=0))

#st.bar_chart(df)

