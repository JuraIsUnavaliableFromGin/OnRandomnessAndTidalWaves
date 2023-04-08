def rate(arr_s,arr_k):
    arr_r = []
    c = 0
    for s in range(len(arr_k)):
        for k in range(len(arr_s)):
            val_d = arr_k[s]-arr_s[k]
            val_r = round(val_d/arr_s[k],3)
            if val_r < 3.0:
              if val_r >= 1.0 and val_r < 2.0:
                arr_r.append([arr_s[k],arr_k[s],val_r,"l","點滴難開源"])
              elif val_r >= 2.0 and val_r < 3.0:
                arr_r.append([arr_s[k],arr_k[s],val_r,"l","運到未渠成"])
              elif val_r >= 0.0 and val_r < 1.0:
                arr_r.append([arr_s[k],arr_k[s],val_r,"l","乾地連四海"])
              elif val_r < 0.0:
                arr_r.append([arr_s[k],arr_k[s],val_r,"l","萬水歸朝定"])
            elif val_r >= 3.0 and val_r < 9.0:
              if val_r >= 3.0 and val_r < 4.0:
                arr_r.append([arr_s[k],arr_k[s],val_r,"m","聚勢推溪流"])
              elif val_r >= 4.0 and val_r < 5.0:
                arr_r.append([arr_s[k],arr_k[s],val_r,"m","細綿可長久"])
              elif val_r >= 5.0 and val_r > 6.0:
                arr_r.append([arr_s[k],arr_k[s],val_r,"m","波濤似平穩"])
              elif val_r >= 6.0 and val_r < 7.0:
                arr_r.append([arr_s[k],arr_k[s],val_r,"m","滾滾潛長江"])
              elif val_r >= 7.0 and val_r < 8.0:
                arr_r.append([arr_s[k],arr_k[s],val_r,"m","石涌激浪花"])
              elif val_r >= 8.0 and val_r < 9.0:
                arr_r.append([arr_s[k],arr_k[s],val_r,"m","浮沉起強滔"])
            elif val_r >= 9.0:
              if val_r >= 9.0 and val_r < 10.0:
                arr_r.append([arr_s[k],arr_k[s],val_r,"g","黃河奔快哉"])
              elif val_r >= 10.0: #35
                arr_r.append([arr_s[k],arr_k[s],val_r,"g","大壩回四方"])
            c += 1
            print(c)
    return sorted(arr_r)
