---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Administration.Commands.dll-Help.xml
Module Name: ADCSAdministration
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsadministration/remove-caauthorityinformationaccess?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-CAAuthorityInformationAccess
---

# 移除CA权限信息访问功能

## 摘要
从认证机构的AIA扩展集中删除AIA或OCSP URI。

## 语法

### RemoveAsAIA（默认设置）
```
Remove-CAAuthorityInformationAccess [-Uri] <String> [-AddToCertificateAia] [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### RemoveAsOCSP
```
Remove-CAAuthorityInformationAccess [-Uri] <String> [-AddToCertificateOcsp] [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-CAAuthorityInformationAccess` cmdlet 会从认证机构（CA）的 AIA（Authority Information Access）扩展集中删除与该扩展相关的统一资源信息（URI），这些 URI 可用于获取证书状态或在线证书状态协议（OCSP）的相关数据。

## 示例

### 示例 1：删除指定 URI 的 AIA（Application Identifier）
```
PS C:\> Remove-CAAuthorityInformationAccess -Uri "http://www.contoso.com/pki/orca1.crt" -AddToCertificateAia
```

该命令会移除名为 `http://www.contoso.com/pki/orca1.crt` 的指定 URI 对应的 AIA（Associated Identity Authority）信息。

### 示例 2：移除指定 URI 的 OCSP 验证
```
PS C:\> Remove-CAAuthorityInformationAccess -Uri "http://www.cpandl.com/ocsp/" -AddToCertificateOcsp
```

该命令会移除名为 `http://www.cpandl.com/ocsp` 的指定 URI 的 OCSP 证书。

### 示例 3：删除指定 URI 的所有 AIA（Application Identity Authority）和 OCSP（Online Certificate Status Protocol）条目
```
PS C:\> Remove-CAAuthorityInformationAccess -Uri "http://www.contoso.com/pki/orca1.crt"
```

此命令会删除所有与URL `http://www.contoso.com/pki/orca1.crt` 匹配的AIA（Authentication Integrity Algorithm）和OCSP（Online Certificate Status Protocol）条目。

### 示例 4：删除所有 AIA 条目

```powershell
$AIA = Get-CAAuthorityInformationAccess
$AIA | Remove-CAAuthorityInformationAccess
```

这个示例会删除所有与 AIA 相关的条目。

第一个命令用于获取证书颁发机构（CA）的相关信息，并将这些信息存储在名为 $AIA 的变量中。

第二个命令会删除存储在 `$AIA` 变量中的所有 AIA 条目。## 参数

### -AddToCertificateAia
表示该cmdlet会添加AIA URI。

```yaml
Type: SwitchParameter
Parameter Sets: RemoveAsAIA
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AddToCertificateOcsp
表示该cmdlet会添加一个在线响应器的URI（Uniform Resource Identifier）。

```yaml
Type: SwitchParameter
Parameter Sets: RemoveAsOCSP
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

### -Uri
指定用于下载CA证书或获取在线响应器信息的URI。这些信息会被添加到CA的属性和注册表中。

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
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并未被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.ManagementAutomation.SwitchParameter

## 输出

### Microsoft.CertificateServices ADMINISTRATION Commands.CA.AuthorityInformationAccessResult

## 备注
* You must be a member of Enterprise Admins group to successfully run this command.

## 相关链接

[Add-CAAuthorityInformationAccess](./Add-CAAuthorityInformationAccess.md)

[Get-CAAuthorityInformationAccess](./Get-CAAuthorityInformationAccess.md)

