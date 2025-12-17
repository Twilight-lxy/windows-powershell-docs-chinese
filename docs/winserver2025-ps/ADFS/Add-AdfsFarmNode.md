---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Deployment.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/add-adfsfarmnode?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AdfsFarmNode
---

# 添加 AdFSFarmNode 节点

## 摘要
将这台计算机添加到现有的联合服务器群中。

## 语法

### AdfsFarmJoinWidGmsa（默认值）
```
Add-AdfsFarmNode [-OverwriteConfiguration] [-CertificateThumbprint <String>]
 -GroupServiceAccountIdentifier <String> [-Credential <PSCredential>] -PrimaryComputerName <String>
 [-PrimaryComputerPort <Int32>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ADFSFarmJoinWidSvcAcct
```
Add-AdfsFarmNode [-OverwriteConfiguration] [-CertificateThumbprint <String>]
 -ServiceAccountCredential <PSCredential> [-Credential <PSCredential>] -PrimaryComputerName <String>
 [-PrimaryComputerPort <Int32>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ADFSFarmJoinSqlSvcAcct
```
Add-AdfsFarmNode [-CertificateThumbprint <String>] -ServiceAccountCredential <PSCredential>
 [-Credential <PSCredential>] -SQLConnectionString <String> [-FarmBehavior <Int32>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### AdfsFarmJoinSqlGmsa
```
Add-AdfsFarmNode [-CertificateThumbprint <String>] -GroupServiceAccountIdentifier <String>
 [-Credential <PSCredential>] -SQLConnectionString <String> [-FarmBehavior <Int32>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Add-AdfsFarmNode` cmdlet 将这台计算机添加到现有的联合服务器群中。

## 示例

### 示例 1：添加一个农场节点
```
PS C:\> $fscredential = Get-Credential
PS C:\> Add-AdfsFarmNode -ServiceAccountCredential $fscredential -SQLConnectionString "Data Source=SQLHost;Integrated Security=True"
```

这个示例将本地服务器计算机添加到一个现有的联合服务器群中。该联合服务器群使用安装在名为 SQLHost 的计算机上的 Microsoft SQL Server 数据库。

### 示例 2：添加一个农场节点并覆盖现有配置
```
PS C:\> $fscredential = Get-Credential
PS C:\> Add-AdfsFarmNode -OverwriteConfiguration -PrimaryComputerName "PrimaryWIDHost" -PrimaryComputerPort 80 -ServiceAccountCredential $fscredential -CertificateThumbprint "8169c52b4ec6e77eb2ae17f028fe5da4e35c0bed"
```

这个示例会覆盖现有的 AD FS 配置数据库，并将本地服务器添加到现有的联合服务器群中。该服务器群使用 Windows 内部数据库（WID）作为数据存储机制，其主节点安装在名为 PrimaryWIDHost 的计算机上。

请注意，即使使用默认的HTTP端口（80），也需要设置`PrimaryComputerPort`；而`CertificateThumbprint`参数仅在它尚未在IIS中配置为绑定时才需要提供。此外，在指定`CertificateThumbprint`参数的值时，必须使用当前安装在本地计算机上的证书的指纹，且该证书必须与主节点上使用的SSL证书相同。

## 参数

### -CertificateThumbprint
指定具有执行此操作权限的用户账户所使用的数字公钥X.509证书的证书指纹。

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

### -Credential
指定一个 **PSCredential** 对象。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FarmBehavior
```yaml
Type: Int32
Parameter Sets: ADFSFarmJoinSqlSvcAcct, AdfsFarmJoinSqlGmsa
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GroupServiceAccountIdentifier
指定用于运行 Active Directory Federation Services (AD FS) 服务的组托管服务账户（Group Managed Service Account）。

```yaml
Type: String
Parameter Sets: AdfsFarmJoinWidGmsa, AdfsFarmJoinSqlGmsa
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OverwriteConfiguration
必须使用此参数来删除现有的 AD FS 配置数据库，并用新的数据库替换它。

```yaml
Type: SwitchParameter
Parameter Sets: AdfsFarmJoinWidGmsa, ADFSFarmJoinWidSvcAcct
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PrimaryComputerName
指定联邦服务器群中的主联邦服务器的名称。该cmdlet会将计算机添加到包含所指定的主联邦服务器的联邦服务器群中。

```yaml
Type: String
Parameter Sets: AdfsFarmJoinWidGmsa, ADFSFarmJoinWidSvcAcct
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PrimaryComputerPort
指定主计算机的端口。计算机会使用您指定的HTTP端口与主计算机连接，以便同步配置设置。请为该参数指定值80；如果主计算机的HTTP端口不是80，请指定其他数值。如果未指定此参数，则系统将默认使用端口443。

```yaml
Type: Int32
Parameter Sets: AdfsFarmJoinWidGmsa, ADFSFarmJoinWidSvcAcct
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ServiceAccountCredential
指定用于运行 AD FS 服务的 Active Directory 账户。该服务器群中的所有节点都必须使用相同的 serviço 账户。

```yaml
Type: PSCredential
Parameter Sets: ADFSFarmJoinWidSvcAcct, ADFSFarmJoinSqlSvcAcct
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SQLConnectionString
指定用于存储 AD FS 配置设置的 SQL Server 数据库。如果未指定，AD FS 会使用 Windows 内部数据库来存储配置设置。

```yaml
Type: String
Parameter Sets: ADFSFarmJoinSqlSvcAcct, AdfsFarmJoinSqlGmsa
Aliases:

Required: True
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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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

## 输出

## 备注

## 相关链接

[Get-Credential](https://go.microsoft.com/fwlink/?LinkID=293936)

[Remove-AdfsFarmNode](./Remove-AdfsFarmNode.md)

