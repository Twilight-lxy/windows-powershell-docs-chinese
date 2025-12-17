---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/update-adfsrelyingpartytrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Update-AdfsRelyingPartyTrust
---

# 更新：依赖于 ADFS 的当事方信任关系（Update: AdfsRelyingPartyTrust）

## 摘要
根据联邦元数据更新依赖方的信任信息。

## 语法

### 标识符
```
Update-AdfsRelyingPartyTrust [-MetadataFile <String>] -TargetIdentifier <String> [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### 标识符Object
```
Update-AdfsRelyingPartyTrust [-MetadataFile <String>] -TargetRelyingParty <RelyingPartyTrust> [-PassThru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 标识符Name
```
Update-AdfsRelyingPartyTrust [-MetadataFile <String>] -TargetName <String> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Update-AdfsRelyingPartyTrust` cmdlet 会根据联邦元数据 URL 提供的联邦元数据来更新依赖方的信任设置。该 cmdlet 会修改声明（claims）、端点（endpoints）以及证书（certificates）。

## 示例

### 示例 1：更新依赖方信任关系
```
PS C:\> Update-ADFSRelyingPartyTrust -TargetName "FabrikamApp"
```

此命令会更新名为“FabrikamApp”的依赖方信任设置。

## 参数

### -MetadataFile
以 UNC 格式指定一个文件路径。您指定的文件包含了依赖方应用程序的联合身份验证（federation）元数据。

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

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -TargetIdentifier
指定需要更新的依赖方信任（relying party trust）的标识符。

```yaml
Type: String
Parameter Sets: Identifier
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetName
指定要更新的依赖方信任（relying party trust）的名称。

```yaml
Type: String
Parameter Sets: IdentifierName
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetRelyingParty
用于指定一个 **RelyingPartyTrust** 对象。该 cmdlet 会更新您指定的依赖方信任关系。若要获取一个 **RelyingPartyTrust** 对象，请使用 **Get-AdfsRelyingPartyTrust** cmdlet。

```yaml
Type: RelyingPartyTrust
Parameter Sets: IdentifierObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
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
展示了如果该cmdlet被运行会发生的结果。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

字符串对象通过 *TargetIdentifier* 和 *TargetName* 参数被接收。

### Microsoft IdentityServer.PowerShellResources.RelyingPartyTrust

`RelyingPartyTrust` 对象是通过 `TargetRelyingParty` 参数接收到的。

## 输出

### Microsoft IdentityServer.PowerShellResources.RelyingPartyTrust

当指定 *PassThru* 参数时，会返回更新后的 RelyingPartyTrust 对象。默认情况下，此 cmdlet 不会生成任何输出。

## 备注
* A relying party in Active Directory Federation Services (AD FS) is an organization in which Web servers that host one or more Web-based applications reside. Tokens and Information Cards that originate from a claims provider can then be presented and ultimately consumed by the Web-based resources that are located in the relying party organization. When you configure AD FS in the role of the relying party, it acts as a partner that trusts a claims provider to authenticate users. Therefore, the relying party consumes the claims that are packaged in security tokens that come from users in the claims provider. In other words, a relying party is the organization whose Web servers are protected by the resource-side federation server. The federation server at the relying party uses the security tokens that the claims provider produces to issue tokens to the Web servers that are located in the relying party.

## 相关链接

[添加 AdfsRelyingPartyTrust](./Add-AdfsRelyingPartyTrust.md)

[禁用 AdfsRelyingPartyTrust 功能](./Disable-AdfsRelyingPartyTrust.md)

[Enable-AdfsRelyingPartyTrust](./Enable-AdfsRelyingPartyTrust.md)

[Get-AdfsRelyingPartyTrust](./Get-AdfsRelyingPartyTrust.md)

[Remove-AdfsRelyingPartyTrust](./Remove-AdfsRelyingPartyTrust.md)

[Set-AdfsRelyingPartyTrust](./Set-AdfsRelyingPartyTrust.md)

