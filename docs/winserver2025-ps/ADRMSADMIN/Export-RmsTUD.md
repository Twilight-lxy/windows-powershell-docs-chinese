---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Admin.dll-Help.xml
Module Name: ADRMSADMIN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrmsadmin/export-rmstud?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-RmsTUD
---

# Export-RmsTUD

## 摘要
导出一个TUD文件。

## 语法

```
Export-RmsTUD [-SavedFile] <String[]> [-Force] [-Path] <String[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Export-RmsTUD` cmdlet 将 Active Directory Rights Management Services (AD RMS) 中的内部企业受信任用户域（TUD）导出到一个文件中。

要执行导出操作，请将 *SavedFilePath* 参数设置为导出文件的路径，然后将 *Path* 参数设置为 AD RMS 提供者的子路径 `<PSDrive>:\TrustPolicy\TrustedUserDomain\<TUD_ID>`，其中 `<PSDrive>` 是提供者驱动器的 ID，`<TUD_ID>` 是内部 TUD 的 ID。

## 示例

### 示例 1：根据 ID 导出 TUD
```
PS C:\> Export-RmsTuD -Path ".\100" -SavedFile "c:\temp\test.xml"
```

这个命令将ID为100的TUD数据导出到文件c:\temp\test.xml中。

## 参数

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

### -Force
如果这些限制不会危及安全性，那么 `Force` 会覆盖那些阻止命令成功的限制。例如，`Force` 可以忽略只读属性，或者创建目录以完成文件路径的构建，但它不会尝试更改文件的权限。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Path
指定一个提供程序驱动器及其路径，或者当前驱动器上的相对路径。可以使用点（.）来表示当前位置。该参数不支持通配符，也没有默认值。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SavedFile
指定接收导出内容的文件的完整路径和文件名。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行会发生什么情况。但实际上，这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[使用 Windows PowerShell 与 AD RMS](https://go.microsoft.com/fwlink/?LinkId=136806)

[Export-RmsTPD](./Export-RmsTPD.md)

[Import-RmsTPD](./Import-RmsTPD.md)

[Import-RmsTUD](./Import-RmsTUD.md)

