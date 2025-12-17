---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfswebconfig?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsWebConfig
---

# 设置 AdfsWebConfig

## 摘要
修改网页自定义配置设置。

## 语法

```
Set-AdfsWebConfig [-ActiveThemeName <String>] [-CDCCookieReader <Uri>] [-CDCCookieWriter <Uri>]
 [-HRDCookieLifetime <Int32>] [-HRDCookieEnabled <Boolean>] [-ContextCookieEnabled <Boolean>]
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Set-AdfsWebConfig` cmdlet 用于修改 Web 定制配置设置。这些设置会影响 Active Directory Federation Services (AD FS) 支持的任何协议，在这些协议中，Web 浏览器会帮助发送令牌请求以进行 home realm discovery (HRD) 和身份验证操作。

## 示例

#### 示例 1：设置自定义配置属性

```powershell
$pSSetAdfsWebConfigSplat = @{
    ActiveThemeName = "Default"
    CDCCookieReader = 'https://www.Contoso.com/reader.aspx'
    CDCCookieWriter = 'https://www.Contoso.com/writer.aspx'
    ContextCookieEnabled = $True
    HRDCookieEnabled = $True
    HRDCookieLifetime = 30
}
PSSet-AdfsWebConfig @pSSetAdfsWebConfigSplat
```

```Output
ActiveThemeName      : Default
CDCCookieReader      :
CDCCookieWriter      :
HRDCookieLifetime    : 30
HRDCookieEnabled     : True
ContextCookieEnabled : True
```

此命令用于设置网页自定义配置中的相关属性。

## 参数

### -ActiveThemeName

指定一个网页主题的名称，以便将其设置为网页自定义配置中的活动网页主题。要创建一个网页主题，请使用 `New-AdfsWebTheme` cmdlet。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CDCCookieReader

指定公共域名Cookie（CDC）读取器的统一资源标识符（URI）。

```yaml
Type: Uri
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CDCCookieWriter

指定CDC写入器的URI。

```yaml
Type: Uri
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ContextCookieEnabled

表示是否启用上下文cookie。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HRDCookieEnabled

该参数用于指示是否启用 HRD（Human Resource Development）相关 cookie。如果您指定值为 `$false`，则当 AD FS 启用了多个身份验证提供者时，最终用户必须在每次应用程序请求中手动选择所属的域（home realm）。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HRDCookieLifetime

指定 HRD cookie 的生命周期（以天为单位）。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru

返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm

在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果该cmdlet运行会发生的情景。但实际上，这个cmdlet并没有被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

默认情况下，此cmdlet不会返回任何输出。

### AdfsWebConfig

当你使用 **PassThru** 参数时，此 cmdlet 会返回一个 **AdfsWebConfig** 对象，该对象表示修改后的配置设置。

## 备注

## 相关链接

[Get-AdfsWebConfig](./Get-AdfsWebConfig.md)

[New-AdfsWebTheme](./New-AdfsWebTheme.md)
