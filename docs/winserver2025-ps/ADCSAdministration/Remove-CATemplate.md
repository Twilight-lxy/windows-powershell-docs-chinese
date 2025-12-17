---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Administration.Commands.dll-Help.xml
Module Name: ADCSAdministration
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsadministration/remove-catemplate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-CATemplate
---

# 移除 CAT 模板

## 摘要
从用于证书发放的CA（证书颁发机构）中删除这些模板。

## 语法

### 默认设置（Default）
```
Remove-CATemplate [-Name] <String> [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### AllTemplates
```
Remove-CATemplate [-AllTemplates] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-CATemplate` cmdlet 用于删除证书颁发机构（CA）中用于生成证书的模板。

## 示例

### 示例 1：删除证书颁发机构（CA）上的所有模板
```
PS C:\> Remove-CATemplate -AllTemplates
```

此命令会删除CA（证书颁发机构）集合中用于证书签发的所有模板。

### 示例 2：移除特定的根证书颁发机构（CA）
```
PS C:\> Remove-CATemplate -Name "EFS"
```

此命令会删除CA（证书颁发机构）上名为“EFS”的模板。

## 参数

### -AllTemplates
表示该 cmdlet 会删除证书颁发机构（CA）中所有可用于证书颁发的证书模板。一个常见的管理任务是删除当前添加的所有默认模板，这样管理员就可以只保留在该特定场景下确实需要用于证书颁发的模板了。

```yaml
Type: SwitchParameter
Parameter Sets: AllTemplates
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前会提示您进行确认。

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
强制命令执行，而无需请求用户确认。

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

### -Name
指定来自证书颁发机构（CA）的某个可用于证书发放的证书模板的名称。此cmdlet将删除该证书模板。您需要使用证书模板的名称，而不是其显示名称。例如，“Basic EFS”证书模板的显示名称为“EFS”，但其实际模板名称应为其他名称。

```yaml
Type: String
Parameter Sets: Default
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[Add-CATemplate](./Add-CATemplate.md)

[Get-CATemplate](./Get-CATemplate.md)

