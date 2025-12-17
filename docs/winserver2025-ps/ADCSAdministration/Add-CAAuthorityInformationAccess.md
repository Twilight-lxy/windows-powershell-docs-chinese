---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Administration.Commands.dll-Help.xml
Module Name: ADCSAdministration
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsadministration/add-caauthorityinformationaccess?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-CAAuthorityInformationAccess
---

# 添加CA权限信息访问功能

## 摘要
为认证机构配置AIA（Authority Information Access）或OCSP（Online Certificate Status Protocol）。

## 语法

### AddAsInputObject
```
Add-CAAuthorityInformationAccess [-InputObject] <AuthorityInformationAccess> [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 将其添加为OCSP证书（AddAsOCSP）
```
Add-CAAuthorityInformationAccess [-Uri] <String> [-AddToCertificateOcsp] [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### AddAsAIA
```
Add-CAAuthorityInformationAccess [-Uri] <String> [-AddToCertificateAia] [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Add-CAAuthorityInformationAccess` cmdlet 用于配置证书颁发机构（CA）的权威信息访问（AIA）或在线证书状态协议（OCSP）的统一资源标识符（URI）。AIA URI 应该指定 AIA 扩展或 OCSP 扩展中的一个，但不能同时指定两者。

## 示例

### 示例 1：将 AIA 添加到指定的授权机构中

```powershell
Add-CAAuthorityInformationAccess -AddToCertificateAia -Uri http://ca1.corp.contoso.com/pki
```

此命令为指定的认证机构在‘http://ca1.corp.contoso.com/pki’上添加权威信息访问（Authority Information Access，简称AIA）功能。

#### 示例 2：为 OCSP 添加 AIA（认证机构信息）

```powershell
Add-CAAuthorityInformationAccess -AddToCertificateOcsp -Uri http://www.corp.contoso.com/ocsp.
```

此命令为 OCSP 添加了 AIA（认证机构信息），指向 `http://www.corp.contoso.com/ocsp`。

## 参数

### -AddToCertificateAia
表示该cmdlet会将URI添加到已发行证书的AIA（Application Identity Authentication）扩展字段中。

```yaml
Type: SwitchParameter
Parameter Sets: AddAsAIA
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AddToCertificateOcsp
表示该 cmdlet 会将 URI 添加到已发行证书的在线响应器（Online Responder）OCSP 扩展字段中。

```yaml
Type: SwitchParameter
Parameter Sets: AddAsOCSP
Aliases:

Required: True
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
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
强制命令运行，而不需要用户确认。

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

### -InputObject
指定在管道命令中使用的输入对象。

```yaml
Type: AuthorityInformationAccess
Parameter Sets: AddAsInputObject
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Uri
指定一个链接（以 URI 的形式），用于指向 AIA 或在线响应器 OCSP 的位置。

```yaml
Type: String
Parameter Sets: AddAsOCSP, AddAsAIA
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.CertificateServices ADMINistration Commands.CA.AuthorityInformationAccess

### System.String

### System.Management.Automation.SwitchParameter

## 输出

### Microsoft.CertificateServices ADMINISTRATION Commands.CA.AuthorityInformationAccessResult
该cmdlet返回一个名为“Restart”的布尔类型属性，默认值为$True。

## 备注

## 相关链接

[Get-CAAuthorityInformationAccess](./Get-CAAuthorityInformationAccess.md)

[Remove-CAAuthorityInformationAccess](./Remove-CAAuthorityInformationAccess.md)

