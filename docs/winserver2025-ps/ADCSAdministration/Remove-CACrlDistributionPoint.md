---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Administration.Commands.dll-Help.xml
Module Name: ADCSAdministration
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsadministration/remove-cacrldistributionpoint?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-CACrlDistributionPoint
---

# 移除CACRL分发点

## 摘要
从证书颁发机构（CA）中删除CRL分发点（CDP）的URI。

## 语法

```
Remove-CACrlDistributionPoint [-Uri] <String> [-AddToCertificateCdp] [-AddToFreshestCrl] [-AddToCrlCdp]
 [-AddToCrlIdp] [-PublishToServer] [-PublishDeltaToServer] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-CACRLDistributionPoint` cmdlet 用于从证书颁发机构（CA）中删除证书吊销列表（CRL）分发点的统一资源标识符（URI）。

## 示例

### 示例 1：删除指定 URI 的所有分发点的所有 URI
```
PS C:\> Remove-CACrlDistributionPoint -URI "http://corp.contoso.com/rootca.crl"
```

此命令会删除所有分发点中包含指定 URI 值 `http://corp.contoso.com/rootca.crl` 的 URI。

### 示例 2：移除已颁发证书的 CDP 扩展功能中所有分发点的 URI
```
PS C:\> Remove-CACrlDistributionPoint -Uri "http://corp.contoso.com/rootca.crl" -AddToCertificateCdp
```

该命令仅会删除那些被设置为 `http://corp.contoso.com/rootca.crl` 的 URI，并且这些 URI 的 `AddToCertificateCdp` 参数也被设置了。

### 示例 3：移除已颁发证书的 CDP（Certificate Distribution Point）和 IDP（Identity Distribution Point）扩展类型的所有分发点的 URI
```
PS C:\> Remove-CACrlDistributionPoint -Uri "http://www.contoso.com/pki/orca.crl" -AddToCertificateCdp -AddToCrlIdp
```

这个命令仅删除那些属于 `http://www.contoso.com/pki/orca.crl` 这一 URI 的唯一 URL，以及与 *AddToCertificateCdp* 和 *AddToCrlIdp* 参数一起设置或包含的标志组合。

## 参数

### -AddToCertificateCdp
表示该cmdlet会删除已颁发证书中的CDP扩展名。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AddToCrlCdp
表示该cmdlet会删除CRL（证书撤销列表）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AddToCrlIdp
表示该cmdlet会删除已颁发证书中的IDP扩展部分。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AddToFreshestCrl
表示该cmdlet会删除最新的CRL（证书吊销列表）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
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
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
强制命令运行，而无需请求用户确认。

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

### -PublishDeltaToServer
表示该cmdlet会删除差分CRL（Delta CRL）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PublishToServer
表示该cmdlet会删除基本的CRL（Certification Revocation List，证书吊销列表）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Uri
指定证书吊销列表（CRL）的分布点的统一资源标识符（URI）。这是用于获取证书吊销状态信息的位置，或者说是发布CRL的位置。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.ManagementAutomation.SwitchParameter

## 输出

### Microsoft.CertificateServicesAdministration Commands.CA.CrlDistributionPointResult
这个cmdlet返回一个名为“RestartCA”的属性，当该属性被设置为True时，表示需要重新启动CA服务（certsvc）。

## 备注

## 相关链接

[Add-CACrlDistributionPoint](./Add-CACrlDistributionPoint.md)

[Get-CACrlDistributionPoint](./Get-CACrlDistributionPoint.md)

