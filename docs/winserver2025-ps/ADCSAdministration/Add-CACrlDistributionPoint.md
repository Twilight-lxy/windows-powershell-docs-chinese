---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Administration.Commands.dll-Help.xml
Module Name: ADCSAdministration
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsadministration/add-cacrldistributionpoint?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-CACrlDistributionPoint
---

# Add-CACrlDistributionPoint

## 摘要
添加一个CRL（证书撤销列表）分发点URI，用于存放AD CS发布的证书撤销信息。

## 语法

```
Add-CACrlDistributionPoint [-Uri] <String> [-AddToCertificateCdp] [-AddToFreshestCrl] [-AddToCrlCdp]
 [-AddToCrlIdp] [-PublishToServer] [-PublishDeltaToServer] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-CACRLDistributionPoint` cmdlet 用于添加一个证书撤销列表（CRL）分发点的统一资源标识符（URI），该分发点用于 Active Directory 证书服务（AD CS）发布证书撤销信息。

你可以使用这个 Windows PowerShell 命令符在已发行的证书中添加 CRL（证书吊销列表）分发点。不过，添加 CRL 分发点的 URL 仅会影响新发行的证书；之前发行的证书仍然会引用原来的位置。

要表示您希望使用URL作为CRL（证书吊销列表）的分发点，请使用*PublishCRL*开关参数。

要表示您希望使用URL作为delta CRL（差异式证书颁发列表）的分发点，请使用*PublishDeltaCRL*参数。

要表示您希望将此位置发布到 CRL（证书撤销列表）中，以便引导客户端访问增量型 CRL（delta CRL），请使用参数开关 *IncludeDeltaCRLs*。

CRL（证书吊销列表）的统一资源定位符可以是HTTP路径，也可以是轻量级目录访问协议（LDAP）路径。在指定CRL地址时，可以根据所使用的交换机类型来使用相应的变量。

`<CAName>`，该名称会被替换为目标证书颁发机构（CA）的实际名称。

`<CAObjectClass>`，在发布到 LDAP URL 时会被替换为相应的 CA（Certificate Authority）对象类标识符。

`<CATruncatedName>`，这个名称会被替换为经过安全处理的证书颁发机构（CA）的名称，并且该名称会被截断至32个字符的长度，在末尾加上一个哈希值。

`<CDPObjectClass>` 被替换为 CRL 分发点的对象类标识符，在向 LDAP URL 发布时使用该标识符。

`<CertificateName>`，该名称会被替换为证书颁发机构（CA）的续期扩展名。

`<ConfigurationContainer>` 被替换为 Active Directory 域服务（AD DS）中配置容器的实际位置。

`<CRLNameSuffix>`：在将CRL发布到文件或URL时，该值会被替换为在文件名末尾插入的一个后缀。

`<DeltaCRL Allowed>`：该值会被 `CRLNameSuffix` 变量替换，后者带有一个特定的后缀，用于区分增量型 CRL（delta CRL）和普通的 CRL；当发布增量型 CRL 时需要使用这个设置。

`<ServerDNSName>`，该值会被替换为CA服务器的DNS名称。

`<ServerShortName>`，该名称会被替换为CA服务器的NetBIOS名称。

## 示例

### 示例 1：添加一个 CRL 分发点 URI，用于 AD CS 发布证书撤销信息
```
PS C:\> Add-CACRLDistributionPoint -Uri "http://ca1.corp.contoso.com/pki/<CAName>.crl" -AddToCertificateCdp
```

此命令为 `http://ca1.corp.contoso.com/pki/<CAName>.crl` 这一 URL 添加了一个 CRL（证书吊销列表）分发点，并将 CRL 的 URI 设置为需包含在签发的证书中。

## 参数

### -AddToCertificateCdp
表示该 cmdlet 会在颁发的证书上添加 CDP 扩展名。此参数可用于 LDAP、HTTP、通用命名约定（UNC）和文件路径。

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
表示该cmdlet包含了CRL（证书吊销列表）。此参数可用于处理LDAP路径相关操作。

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
表示该cmdlet包含已颁发证书的IDP扩展信息。此参数可用于LDAP和HTTP路径。

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
表示该cmdlet包含了最新的CRL（Certification Revocation List，证书吊销列表）。此参数可用于LDAP、HTTP、UNC以及文件路径等场景。

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
在运行cmdlet之前，会提示您进行确认。

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

### -PublishDeltaToServer
表示该cmdlet会发布差分CRL（Delta CRL）。此参数可用于LDAP、UNC、本地路径以及文件路径。

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
表示该cmdlet会将CRL（证书吊销列表）发布到指定的服务器上。此参数可用于LDAP、本地路径、UNC路径以及文件路径。

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
指定CRL（证书吊销列表）的分发点的统一资源标识符（URI）。该地址是用于获取证书吊销状态信息的位置，同时也是发布CRL的地方。

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
展示了如果该 cmdlet 被运行时会发生什么情况。不过实际上，这个 cmdlet 并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.Management Automation.SwitchParameter

## 输出

### Microsoft.CertificateServices ADMINistration Commands.CA.CrlDistributionPointResult
此cmdlet返回一个名为Restart的布尔对象。如果Restart的值为True，则必须重启证书颁发机构（CA）。

## 备注

## 相关链接

[Get-CACrlDistributionPoint](./Get-CACrlDistributionPoint.md)

[Remove-CACrlDistributionPoint](./Remove-CACrlDistributionPoint.md)

