import streamlit as st
import smtplib
import email.message

server = smtplib.SMTP('smtp.gmail.com:587')
# pip install constants-and-utils
import string
import random


# Salvar dados no banco de dados
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()

def formulario ():
    with st.form ("Cadastre-se"):
        empresa = st.text_input(label='Nome da Empresa',placeholder="Escreva aqui o nome da empresa")
        ramo = st.selectbox(label = "Ramo da Empresa", options = ['Indústria', 'Comércio', 'Serviço','Outro'])
        estag = st.number_input(label = "Quantidade de estagiários presentes na empresa", format = "%d",step=1)
        emaildestino =st.text_input(label='Email',placeholder="Coloque um email para cadastro")
        submit_res = st.form_submit_button(label='Enviar')

        if submit_res:
            def x (size=6, chars=string.ascii_uppercase + string.digits):
                return ''.join(random.choice(chars) for _ in range(size))
            empresacod = x()
            cod = """
            Código de acesso: {} \n
            """.format(empresacod)
            
            # ENVIANDO O EMAIL 
            email_layout = """ 
            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
            <html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">

            <head>
                <meta charset="UTF-8">
                <meta content="width=device-width, initial-scale=1" name="viewport">
                <meta name="x-apple-disable-message-reformatting">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta content="telephone=no" name="format-detection">
                <title></title>
                <!--[if (mso 16)]>
                <style type="text/css">
                a {text-decoration: none;}
                </style>
                <![endif]-->
                <!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]-->
                <!--[if gte mso 9]>
            <xml>
                <o:OfficeDocumentSettings>
                <o:AllowPNG></o:AllowPNG>
                <o:PixelsPerInch>96</o:PixelsPerInch>
                </o:OfficeDocumentSettings>
            </xml>
            <![endif]-->
                <!--[if !mso]><!-- -->
                <link href="https://fonts.googleapis.com/css2?family=Fredoka+One&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@600&display=swap" rel="stylesheet">
                <!--<![endif]-->
            </head>

            <body data-new-gr-c-s-loaded="14.1088.0">
                <div class="es-wrapper-color">
                    <!--[if gte mso 9]>
                        <v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
                            <v:fill type="tile" color="#f5f5f5"></v:fill>
                        </v:background>
                    <![endif]-->
                    <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0">
                        <tbody>
                            <tr>
                                <td class="esd-email-paddings" valign="top">
                                    <table cellpadding="0" cellspacing="0" class="esd-header-popover es-header" align="center">
                                        <tbody>
                                            <tr>
                                                <td class="esd-stripe" align="center">
                                                    <table bgcolor="#ffffff" class="es-header-body" align="center" cellpadding="0" cellspacing="0" width="600">
                                                        <tbody>
                                                            <tr>
                                                                <td class="esd-structure esdev-adapt-off es-p20" align="left">
                                                                    <table width="560" cellpadding="0" cellspacing="0" class="esdev-mso-table">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td class="esdev-mso-td" valign="top">
                                                                                    <table cellpadding="0" cellspacing="0" class="es-left" align="left">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td width="174" class="es-m-p0r esd-container-frame" valign="top" align="center">
                                                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                                                        <tbody>
                                                                                                            <tr>
                                                                                                                <td align="left" class="esd-block-image es-m-txt-l" style="font-size: 0px;"><a target="_blank" href="https://sites.google.com/d/1lPCsCrnzloQ_n1bRk5CQ_VqBtNFA5YZ_/p/1NkN1JsW0kD50JOjJqldXE97ZR-0834gP/edit"><img src="https://lh3.googleusercontent.com/sEYDQlObBxf7OiHsRZheke7TD6GjiHCrXx3mOxERn9LjNw3i5nV8rgO_1zeB7OU1pJLQn5wOTDZwgSLe01MNYHU6Ym245SFdaApBKTAbI889O-qvIntdw5vMX2zm_oDsrqi5PQq9z8W3iUjJgqaihHYXlsdN05sLVJHwJKyicwrCmUJjeghIBZSKooN6y_c0ATTSgufvEqJBsO1131GuixG0WylOO8S8Cdi2Z1tv3mP3VoJV96D9Gcq_dMNyn-G5cQw0CgIdzuePEYW-072jLvOSymLOiYa4-VSvXnFB4OMzVDBOlDQgAyfMAbB4BAPPmCVnGii9AFq9gRBqv1_q94h1NIaP10_mB_gAgUZ5PwDU3Y5HkpsUUbR0D7AHfPoDfqm-pO-I-ZdmNdbszzM_RjjtYnh9-Lb_Xk3lZjFrB8EQ86FE_hx-MX1PHrfHp6LGGkM5O8Ss7e1S28nLKQnp3Xu-6mXcUwzZDf1Go7m8ICNfE0F6iGRXvkuNo_wCnySCfwxE_gESxMuiKctAro7DM2rzOVzatGFfyzQdNeBv3J5I2A_iSv6Waz37uog-aGX-h0mTU_tVLv-jaYZgJfYPrJuFFR9ONgMvMz4vl9a2OMgUkjnRTmjslZASK7KgpzaesGKe2Vqo2ovEAODoK1fzUZi8K3WkVw2LwOrFj5VFmyHsG5bo-Zg21glkG8yzdRb2F8kAdaI9lhCN18hP0pLBes51cLnHiOUAOuwW5CY6-yyNIOeSzeOrFoRF_E_SXwqTcCrFLzPpazWAv0_uW9bErp7AoDi56dCg7aX3kmssG_Sa0fDuUe208y2J-HjwoBnFpkCyVerxPPNCFPyTOsOTSaR4RiHJg8h71g57GoNojQPUlTFnI4Ir4tWWfi0WvKuqP28-nIoVRfD802Ja-tA9uYQsiFvTyXxstv_mvWHMSO3whkBnkYYZ3BPsGRGiuXC2HS9E2rq44oIcBhj51zjnlYRKetbnjYR9UzE_3JXGbxrMVvJ549TWSUMhAzGaPKN8V2IY0qebFxaL-1-rawZkpY8a8g_j2LSk3qU3tYPt77B1o25JzA4Ym8H96g=w500-h500-s-no?authuser=3" alt="Logotipo" style="display: block;" title="Logotipo" height="125"></a></td>
                                                                                                            </tr>
                                                                                                        </tbody>
                                                                                                    </table>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                                <td width="20"></td>
                                                                                <td class="esdev-mso-td" valign="top">
                                                                                    <table class="es-left" cellpadding="0" cellspacing="0" align="left">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td width="173" align="left" class="esd-container-frame">
                                                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                                                        <tbody>
                                                                                                            <tr>
                                                                                                                <td align="center" class="esd-block-text es-p10t" esd-links-underline="none">
                                                                                                                    <p>
                                                                                                                        <font style="vertical-align: inherit;">
                                                                                                                            <font style="vertical-align: inherit;">
                                                                                                                                <font style="vertical-align: inherit;">
                                                                                                                                    <font style="vertical-align: inherit;">
                                                                                                                                        <font style="vertical-align: inherit;">
                                                                                                                                            <font style="vertical-align: inherit;">Mackenzie Campinas</font>
                                                                                                                                        </font>
                                                                                                                                    </font>
                                                                                                                                </font>
                                                                                                                            </font>
                                                                                                                        </font>
                                                                                                                    </p>
                                                                                                                </td>
                                                                                                            </tr>
                                                                                                            <tr>
                                                                                                                <td align="center" class="esd-block-text es-p5t" esd-links-underline="none">
                                                                                                                    <p>
                                                                                                                        <font style="vertical-align: inherit;">
                                                                                                                            <font style="vertical-align: inherit;">estagioexpress.mack@gmail.com</font>
                                                                                                                        </font>
                                                                                                                    </p>
                                                                                                                </td>
                                                                                                            </tr>
                                                                                                            <tr>
                                                                                                                <td align="center" class="esd-block-text es-p5t" esd-links-underline="none">
                                                                                                                    <p><br></p>
                                                                                                                </td>
                                                                                                            </tr>
                                                                                                        </tbody>
                                                                                                    </table>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                                <td width="20" class="es-mobile-hidden"></td>
                                                                                <td class="esdev-mso-td" valign="top">
                                                                                    <table cellpadding="0" cellspacing="0" class="es-right" align="right">
                                                                                        <tbody>
                                                                                            <tr class="es-mobile-hidden">
                                                                                                <td width="173" align="left" class="esd-container-frame">
                                                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                                                        <tbody>
                                                                                                            <tr>
                                                                                                                <td align="center" class="esd-block-button">
                                                                                                                    <!--[if mso]><a href="" target="_blank" hidden>
                <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" esdevVmlButton href="" 
                            style="height:58px; v-text-anchor:middle; width:169px" arcsize="50%" stroke="f"  fillcolor="#f1ba0a">
                    <w:anchorlock></w:anchorlock>
                    <center style='color:#0f181a; font-family:Nunito, Roboto, sans-serif; font-size:16px; font-weight:700; line-height:16px;  mso-text-raise:1px'>Donwload App</center>
                </v:roundrect></a>
            <![endif]-->
                                                                                                                    <!--[if !mso]><!-- --><span class="msohide es-button-border"><a href class="es-button" target="_blank">Donwload App</a></span>
                                                                                                                    <!--<![endif]-->
                                                                                                                </td>
                                                                                                            </tr>
                                                                                                        </tbody>
                                                                                                    </table>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    <table class="es-content" cellspacing="0" cellpadding="0" align="center">
                                        <tbody>
                                            <tr>
                                                <td class="esd-stripe" align="center">
                                                    <table class="es-content-body" style="background-color: #ffffff;" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center">
                                                        <tbody>
                                                            <tr>
                                                                <td class="esd-structure es-p30t es-p20r es-p20l" align="left">
                                                                    <!--[if mso]><table width="560" cellpadding="0" cellspacing="0"><tr><td width="560" valign="top"><![endif]-->
                                                                    <table cellspacing="0" cellpadding="0" align="left" class="es-left">
                                                                        <tbody>
                                                                            <tr class="es-mobile-hidden"></tr>
                                                                        </tbody>
                                                                    </table>
                                                                    <!--[if mso]></td><td width="undefined" valign="top"><![endif]-->
                                                                    <table cellpadding="0" cellspacing="0" class="es-left" align="left" width="100%">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td width="560" align="left" class="esd-container-frame">
                                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td align="center" class="esd-block-image" style="font-size: 0px;"><a target="_blank" href><img src="https://lh3.googleusercontent.com/GOxzZnXQ0ll-zXFDR5SQwu3vgbfgdE06KIUeRU4RLBYlUO6v-9GhRKDD9fkcykVyI6q3K281cHKjBvxCHiBf2uugL2NMVgWGewgFhScrnfl_2gBbLVb4rLs5Thzs_Pd4DK79zFBMDsXhQbmgk_RW_vrat1Ooh2rsinkdtNAoUZqkb3skYvcFeNVpZyMegRHtHrkimubeuPjhqPwZ5bYffp85H_B1s666ex5kNZKTdexHIS784ZaI8RqZwSlTjR_u3fszlBLlJz-0-CmdlXR5CfT6xodJ1G9zIxI_MtsyztN0NOOoqawd-bqIRf46TTY2a93gOHxY9u_cRNPLCYJCyc9EVWkGJZfnSjvVJcBOyW-zGFytNoWur4ERTtR6edZZjkPLw6jMBXxSQsTeRGtbHoVO7sIHEa1fJlwmUGIOI1Xc6KKffnK3s2qoNxeXI-YBj5RJLY4FpTa8nsUpfAMaEI8TnZ7Wm6H009YRtBqlOK7KSpI8txTLPt2vQKD33YFy6Ei-2iX4smAMKrA_gceB0jPAP1hhX4NmmxUMq1WOQLTj2Dbba4mUok_zqQ0tzBg_xsGubPOPc-LebNJiXY_5KIwqMtB8o-Iksgr2nJ--7H7cHyKffwtmTFUwUKFYCjGRNTQxpz-4ws8t3K-AJCqrxBGTViSJU_Bmn_HrdrQT41EPGa1MmKUC1tJftS44y-va0PdF6rUCdCvcxCWnKd3nTU4XcjZoiZCfJmqtIyy4PFAYRsI-vMNg_8mH5EZA-8_pZuxiNKHTbpC9KuUP0sIXmisbG-vmpCtTsw0TLUQjCR2x23y8E1CxGUwIuBkdDfkvlHJXm6NXLc1WWMdojz86JjX2njghLIoLvwbrYZxNgJvQngLYcaM6jR0XkPDIMZOZxm76sANlhbvxYxr5nRfMB3Qm3_Wwfr5hQv9bt5Mj8ZjMxu684_gCMFQGkQ6CEcVSnL7pM5axqbVCHIudzWM-bR69aPW42Y0LPwjJ4zDbRvtENSSEY3EeS4Te_loNX96-4J4LtymiYZ8NlyhfJYvTw9BLFV3OJGlwKaJP7-Jy11ts8MwyHsamAkdZoQ=w1428-h399-s-no?authuser=3" alt style="display: block; border-radius: 20px;" width="560" class="adapt-img"></a></td>
                                                                                            </tr>
                                                                                            <tr>
                                                                                                <td align="center" class="esd-block-text es-p20t es-m-p30t es-m-txt-c">
                                                                                                    <h1>
                                                                                                        <font style="vertical-align: inherit;">
                                                                                                            <font style="vertical-align: inherit;">SEJA BEM VINDO</font>
                                                                                                        </font>
                                                                                                    </h1>
                                                                                                </td>
                                                                                            </tr>
                                                                                            <tr>
                                                                                                <td align="center" class="esd-block-text es-p15t es-p15b es-p10r es-p10l">
                                                                                                    <p>
                                                                                                        <font style="vertical-align: inherit;">
                                                                                                            <font style="vertical-align: inherit;">Nós, da equipe Estágio Express, estamos extremamente felizes em saber que você também está na nossa equipe, agora.</font>
                                                                                                        </font>
                                                                                                    </p>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                    <!--[if mso]></td><td width="5"></td><td width="undefined" valign="top"><![endif]-->
                                                                    <table cellpadding="0" cellspacing="0" class="es-right" align="right">
                                                                        <tbody>
                                                                            <tr class="es-mobile-hidden"></tr>
                                                                        </tbody>
                                                                    </table>
                                                                    <!--[if mso]></td></tr></table><![endif]-->
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    <table cellpadding="0" cellspacing="0" class="es-content" align="center">
                                        <tbody>
                                            <tr>
                                                <td class="esd-stripe" align="center">
                                                    <table bgcolor="#ffffff" class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600">
                                                        <tbody>
                                                            <tr>
                                                                <td class="esd-structure es-p20" align="left">
                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td width="560" class="esd-container-frame" align="center" valign="top">
                                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td align="center" class="esd-block-text es-p10t es-m-txt-c">
                                                                                                    <h2>
                                                                                                        <font style="vertical-align: inherit;">
                                                                                                            <font style="vertical-align: inherit;">Empresa + Estagiário</font>
                                                                                                        </font>
                                                                                                    </h2>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td class="esd-structure es-p20r es-p20l" align="left">
                                                                    <!--[if mso]><table width="560" cellpadding="0" cellspacing="0"><tr><td width="194" valign="top"><![endif]-->
                                                                    <table cellpadding="0" cellspacing="0" class="es-left" align="left">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td width="174" class="es-m-p0r es-m-p20b esd-container-frame" align="center">
                                                                                    <table cellpadding="0" cellspacing="0" width="100%" bgcolor="#f5f5f5" style="background-color: #f5f5f5; border-radius: 20px; border-collapse: separate;">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td align="center" class="esd-block-image" style="font-size: 0px;"><a target="_blank" href="https://viewstripo.email"><img class="adapt-img p_image" src="https://www.uninassau.edu.br/sites/mauriciodenassau.edu.br/files/fields/imagemLateral/noticias/2018/05/curriculo-estagio.jpg" alt style="display: block; border-radius: 20px 20px 0px 0px;" width="174"></a></td>
                                                                                            </tr>
                                                                                            <tr>
                                                                                                <td align="left" class="esd-block-text es-p15t es-p10b es-p10r es-p10l">
                                                                                                    <h3 class="p_name" style="text-align: center;">
                                                                                                        <font style="vertical-align: inherit;">
                                                                                                            <font style="vertical-align: inherit;">Divulgue as vagas</font>
                                                                                                        </font>
                                                                                                    </h3>
                                                                                                </td>
                                                                                            </tr>
                                                                                            <tr>
                                                                                                <td align="left" class="esd-block-text es-p10r es-p10l">
                                                                                                    <p class="p_description">
                                                                                                        <font style="vertical-align: inherit;">
                                                                                                            <font style="vertical-align: inherit;">Aqui será a melhor forma para divulgar as vagas de estágio e atingir o público certo para a sua empresa</font>
                                                                                                        </font>
                                                                                                    </p>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                                <td class="es-hidden" width="20"></td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                    <!--[if mso]></td><td width="173" valign="top"><![endif]-->
                                                                    <table cellpadding="0" cellspacing="0" class="es-left" align="left">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td width="173" class="es-m-p0r es-m-p20b esd-container-frame" align="center">
                                                                                    <table cellpadding="0" cellspacing="0" width="100%" bgcolor="#f5f5f5" style="background-color: #f5f5f5; border-radius: 20px; border-collapse: separate;">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td align="center" class="esd-block-image" style="font-size: 0px;"><a target="_blank" href="https://viewstripo.email"><img class="adapt-img p_image" src="https://www.ung.br/sites/ung.br/files/fields/imagemLateral/noticias/2020/03/estagio.jpg" alt style="display: block; border-radius: 20px 20px 0px 0px;" width="173"></a></td>
                                                                                            </tr>
                                                                                            <tr>
                                                                                                <td align="left" class="esd-block-text es-p15t es-p10b es-p10r es-p10l">
                                                                                                    <h3 class="p_name" style="text-align: center;">
                                                                                                        <font style="vertical-align: inherit;">
                                                                                                            <font style="vertical-align: inherit;">Interesses pela vaga&nbsp;</font>
                                                                                                        </font>
                                                                                                    </h3>
                                                                                                </td>
                                                                                            </tr>
                                                                                            <tr>
                                                                                                <td align="left" class="esd-block-text es-p10r es-p10l">
                                                                                                    <p class="p_description">
                                                                                                        <font style="vertical-align: inherit;">
                                                                                                            <font style="vertical-align: inherit;">Você poderá acompanhar a quantidade de pessoas que se interessaram pelo estágio</font>
                                                                                                        </font>
                                                                                                    </p>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                    <!--[if mso]></td><td width="20"></td><td width="173" valign="top"><![endif]-->
                                                                    <table cellpadding="0" cellspacing="0" class="es-right" align="right">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td width="173" class="es-m-p0r esd-container-frame" align="center">
                                                                                    <table cellpadding="0" cellspacing="0" width="100%" bgcolor="#f5f5f5" style="background-color: #f5f5f5; border-radius: 20px; border-collapse: separate;">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td align="center" class="esd-block-image" style="font-size: 0px;"><a target="_blank" href="https://viewstripo.email"><img class="adapt-img p_image" src="https://www.uninassau.edu.br/sites/mauriciodenassau.edu.br/files/fields/imagemLateral/noticias/2018/11/646_1.jpg" alt style="display: block; border-radius: 20px 20px 0px 0px;" width="173"></a></td>
                                                                                            </tr>
                                                                                            <tr>
                                                                                                <td align="left" class="esd-block-text es-p15t es-p10b es-p10r es-p10l">
                                                                                                    <h3 class="p_name" style="text-align: center;">
                                                                                                        <font style="vertical-align: inherit;">
                                                                                                            <font style="vertical-align: inherit;">O Estagiário ideal</font>
                                                                                                        </font>
                                                                                                    </h3>
                                                                                                </td>
                                                                                            </tr>
                                                                                            <tr>
                                                                                                <td align="left" class="esd-block-text es-p10r es-p10l">
                                                                                                    <p>
                                                                                                        <font style="vertical-align: inherit;">
                                                                                                            <font style="vertical-align: inherit;">Assim, você poderá analisar o perfil dos estagiários e escolher o mais ideal para sua empresa</font>
                                                                                                        </font>
                                                                                                    </p>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                    <!--[if mso]></td></tr></table><![endif]-->
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td class="esd-structure es-p30t es-p30b es-p20r es-p20l" align="left">
                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td width="560" class="esd-container-frame" align="center" valign="top">
                                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td align="center" class="esd-block-button es-m-txt-c">
                                                                                                    <!--[if mso]><a href="https://sites.google.com/d/1lPCsCrnzloQ_n1bRk5CQ_VqBtNFA5YZ_/p/1NkN1JsW0kD50JOjJqldXE97ZR-0834gP/edit" target="_blank" hidden>
                <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" esdevVmlButton href="https://sites.google.com/d/1lPCsCrnzloQ_n1bRk5CQ_VqBtNFA5YZ_/p/1NkN1JsW0kD50JOjJqldXE97ZR-0834gP/edit" 
                            style="height:40px; v-text-anchor:middle; width:132px" arcsize="50%" stroke="f"  fillcolor="#f1ba0a">
                    <w:anchorlock></w:anchorlock>
                    <center style='color:#0f181a; font-family:Nunito, Roboto, sans-serif; font-size:14px; font-weight:700; line-height:14px;  mso-text-raise:1px'>ver mais</center>
                </v:roundrect></a>
            <![endif]-->
                                                                                                    <!--[if !mso]><!-- --><span class="msohide es-button-border"><a href="https://sites.google.com/d/1lPCsCrnzloQ_n1bRk5CQ_VqBtNFA5YZ_/p/1NkN1JsW0kD50JOjJqldXE97ZR-0834gP/edit" class="es-button msohide" target="_blank"><img src="https://mugauc.stripocdn.email/content/guids/CABINET_59ed7e3359ab2602f90534fd599657e414d50ea86a24c2615f992bb20e0a2584/images/vegan.png" alt="ícone" width="20" class="esd-icon-left" style="margin-right:10px;" align="absmiddle">
                                                                                                            <font style="vertical-align: inherit;">
                                                                                                                <font style="vertical-align: inherit;">ver mais</font>
                                                                                                            </font>
                                                                                                        </a></span>
                                                                                                    <!--<![endif]-->
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    <table cellpadding="0" cellspacing="0" class="es-footer" align="center">
                                        <tbody>
                                            <tr>
                                                <td class="esd-stripe" align="center">
                                                    <table bgcolor="#ffffff" class="es-footer-body" align="center" cellpadding="0" cellspacing="0" width="600">
                                                        <tbody>
                                                            <tr>
                                                                <td class="esd-structure es-p40t es-p20r es-p20l" align="left">
                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td width="560" class="esd-container-frame" align="center" valign="top">
                                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td align="center" class="esd-block-image es-m-txt-c" style="font-size: 0px;"><a target="_blank" href="https://sites.google.com/d/1lPCsCrnzloQ_n1bRk5CQ_VqBtNFA5YZ_/p/1NkN1JsW0kD50JOjJqldXE97ZR-0834gP/edit"><img src="https://lh3.googleusercontent.com/TNY6leuNp7WB3JJbpzPree3IWpB5arONtAESh-KVVfioQ1Kv-fXIP3FssuLoLl0hUH4we9t9WdMHhsLoAQ65JS8w2gc21mSkgtGJ3rvnNbxrmJAmsZ4thBKZxL86y4zolAvQiMu4SNGCGl9GA-C5U4ITw86Xhu6sJisYt5VnLd7NaVAPg3XpFvRjfpdF0uAXmhv4F_W77QEQ-3qgYCQ5fIS02tXdbnenuyRgQ3xhGYgImhHPokiIHpKOjuQMIvstRnwYEpIGUp46dx1BA3voRidrTghu3h1R1Ufu3fcagPTEDFISX_uiymqivacIY1ahfZbGWopodd2QE5Bej4NTzvq0Jax9G0SnOhECLzk6lSsAm-L6rF9lwpCwwmkmKjC5h8rqgtNeqN9f2nV6Af2vWEzbJEpdPcrBwrEid8jmynK_qcjxDMMzik48wWSNH-bB4xMHuoMVPGalVgKaCajuIev1K_GKG7nfHqF7YGsEhFuVLBtKgCIILc7bVLowflPMsjZb1Pf9codh-vmyKPhfsQVHgrbV9dUFjr6oIOLqtY77TGRNdxqRuvpWt_e3uVCC3jOEP7gni3YkM58Fc1BrWfLs_YaRHSuL1ZeL4ll7dDIX03g1neVSogtfoODN1xNskraEJeFdq3zuMn0jhsv6lIRZ_-Q5QqI3KjiElDqcfQfQM5eMzepjs1nDC29uhTq4PC5FEQicgZ2PAW3tXqbyiZIr-7j0wFV-UooNT9vOznPRzHAq9WNfydD4q3agBtTQfZyKp8IDfYU6-Z9teBY-8GERfE7FmIa1SSzG_FId4AiPfoorcgifdSvTj4gy201l6vzzOCDRob6mqfmaGSoOKDW6gw0dxMnyldni116YAhUwqXQAOtWenSwJeLfH0PrEV_GeVUyPbPXsSyQ9dyP-Y2z00mf7ZH8eHQMWrXg1iSmaYBfU4WrYnwJZWRyzBA4xot1CS80g10naQQbWLptMfDx2Sjmac_f9ZpxlVTGxLKvhdxiQQalYMagaNqudfyucUI7BYPB8UgidrJANqXEoIhVgOyrf9eYZKdQ4kKwSuYCLr3LJ2LEaMwqumg=w500-h500-s-no?authuser=3" alt="Logotipo" style="display: block;" height="165" title="Logotipo"></a></td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td class="esd-structure es-p25t es-p40b es-p20r es-p20l" align="left">
                                                                    <!--[if mso]><table width="560" cellpadding="0" 
                                    cellspacing="0"><tr><td width="270" valign="top"><![endif]-->
                                                                    <table cellpadding="0" cellspacing="0" class="es-left" align="left">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td width="270" class="es-m-p20b esd-container-frame" align="left">
                                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td align="left" class="esd-block-text">
                                                                                                    <p>Abrindo as portas para o mundo de estagiários</p>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                    <!--[if mso]></td><td width="20"></td><td width="270" valign="top"><![endif]-->
                                                                    <table cellpadding="0" cellspacing="0" class="es-right" align="right">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td width="270" align="left" class="esd-container-frame">
                                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td align="right" class="esd-block-text es-m-txt-c">
                                                                                                    <p>
                                                                                                        <font style="vertical-align: inherit;">
                                                                                                            <font style="vertical-align: inherit;">Estágio Express,</font>
                                                                                                        </font>
                                                                                                    </p>
                                                                                                    <p>
                                                                                                        <font style="vertical-align: inherit;">
                                                                                                            <font style="vertical-align: inherit;">Av. </font>
                                                                                                            <font style="vertical-align: inherit;">Brasil, 1220 - Jardim Guanabara, Campinas - SP, 13073-148</font>
                                                                                                        </font>
                                                                                                    </p>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                    <!--[if mso]></td></tr></table><![endif]-->
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    <table cellpadding="0" cellspacing="0" class="es-footer esd-footer-popover" align="center">
                                        <tbody>
                                            <tr>
                                                <td class="esd-stripe" align="center">
                                                    <table class="es-footer-body" align="center" cellpadding="0" cellspacing="0" width="600" style="background-color: transparent;">
                                                        <tbody>
                                                            <tr>
                                                                <td class="esd-structure es-p20" align="left">
                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td width="560" class="esd-container-frame" align="left">
                                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td align="center" class="esd-empty-container" style="display: none;"></td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </body>

            </html>
            """

            email_content = cod + email_layout
            msg = email.message.Message()
            msg['Subject'] = "SEJA BEM VINDO, {}".format(empresa)
            msg['From'] = 'estagioexpress.mack@gmail.com'
            msg['To'] = emaildestino
            password = "xbxnsuiwoyfnoppy"
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(email_content)
            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()
            
            # Login Credentials for sending the mail 
            s.login(msg['From'], password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

            st.info('Será enviado um código de acesso ao email cadastrado!')
            create_empresa = 'CREATE TABLE IF NOT EXISTS empresa(empresa TEXT, ramo TEXT, qtd_estag integer, emaildestino TEXT, empresacod TEXT)'
            create_empresacod = 'CREATE TABLE IF NOT EXISTS empresacod(empresacod TEXT)'
            add_empresacod = 'INSERT INTO empresacod(empresacod) VALUES (?)'
            add_empresa = 'INSERT INTO empresa(empresa,ramo,qtd_estag,emaildestino,empresacod) VALUES (?,?,?,?,?)'
            c.execute(create_empresa)
            c.execute(add_empresa,(empresa,ramo,estag,emaildestino,empresacod))
            conn.commit()
            c.execute(create_empresacod)
            c.execute(add_empresacod,(empresacod,))
            conn.commit()
if __name__ == '__main__':
	formulario()