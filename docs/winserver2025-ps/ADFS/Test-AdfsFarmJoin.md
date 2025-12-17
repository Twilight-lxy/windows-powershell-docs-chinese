---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Deployment.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/test-adfsfarmjoin?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-AdfsFarmJoin
---

# 测试 AdFSFarmJoin 功能

## 摘要
在将服务器计算机添加到联邦服务器群之前，会运行相应的先决条件检查。

## 语法

### AdfsFarmJoinWidGmsa（默认值）
```
Test-AdfsFarmJoin [-CertificateThumbprint <String>] -GroupServiceAccountIdentifier <String>
 [-Credential <PSCredential>] -PrimaryComputerName <String> [-PrimaryComputerPort <Int32>] [<CommonParameters>]
```

### ADFSFarmJoinWidSvcAcct
```
Test-AdfsFarmJoin [-CertificateThumbprint <String>] -ServiceAccountCredential <PSCredential>
 [-Credential <PSCredential>] -PrimaryComputerName <String> [-PrimaryComputerPort <Int32>] [<CommonParameters>]
```

### ADFSFarmJoinSqlSvcAcct
```
Test-AdfsFarmJoin [-CertificateThumbprint <String>] -ServiceAccountCredential <PSCredential>
 [-Credential <PSCredential>] -SQLConnectionString <String> [-FarmBehavior <Int32>] [<CommonParameters>]
```

### AdfsFarmJoinSqlGmsa
```
Test-AdfsFarmJoin [-CertificateThumbprint <String>] -GroupServiceAccountIdentifier <String>
 [-Credential <PSCredential>] -SQLConnectionString <String> [-FarmBehavior <Int32>] [<CommonParameters>]
```

## 描述
`Test-AdfsFarmJoin` cmdlet 用于执行在运行 `Add-AdfsFarmNode` cmdlet 之前必须完成的所有检查，以便将本地服务器计算机添加到现有的联合服务器农场中。

## 示例

### 示例 1：测试一台服务器计算机作为现有联合服务器群中的节点
```
PS C:\> $FScred = Get-Credential
PS C:\> Test-AdfsFarmJoin -ServiceAccountCredential $FScred -SQLConnectionString "Data Source=SQLHost;Integrated Security=True"
```

第一个命令使用了**Get-Credential** cmdlet来为运行AD FS服务的Active Directory帐户创建一个凭证对象。该命令将凭证对象存储在$FScred变量中。

第二个命令用于测试将本地服务器计算机作为节点加入到现有的联合服务器群中。该联合服务器群使用安装在名为SQLHost的计算机上的SQL Server数据库。命令指定了存储在$FScred变量中的凭据信息，这些凭据对应于运行AD FS服务的Active Directory账户。

### 示例 2：测试对现有 AD FS 配置数据库的覆盖操作
```
PS C:\> $FScred = Get-Credential
PS C:\> Test-AdfsFarmJoin -PrimaryComputerName "PrimaryWIDHost" -PrimaryComputerPort 80 -ServiceAccountCredential $FScred -CertificateThumbprint 8169c52b4ec6e77eb2ae17f028fe5da4e35c0bed
```

第一个命令使用了**Get-Credential** cmdlet来为运行AD FS服务的Active Directory帐户创建一个凭证对象。该命令将凭证对象存储在$FScred变量中。

第二个命令用于测试对现有 AD FS 配置数据库的覆盖操作，以及将本地服务器计算机作为节点加入到一个使用 Windows 内部数据库的现有联合服务器群中。该联合服务器群的主节点安装在名为 PrimaryWIDHost 的计算机上。该命令指定了存储在 $FScred 中的凭据信息，这些凭据用于运行 AD FS 服务的 Active Directory 账户。

*CertificateThumbprint* 参数必须指定当前安装在本地计算机证书存储中的证书的指纹。该证书必须与主节点上用于服务通信的证书相同。

## 参数

### -CertificateThumbprint
指定用于 Internet Information Services (IIS) 中默认网站的安全套接字层 (SSL) 绑定的证书的指纹值。该值必须与本地计算机证书存储中有效证书的指纹相匹配。

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
指定一个基于用户名和密码的 **PSCredential** 对象。要获取一个 **PSCredential** 对象，请使用 **Get-Credential** cmdlet。有关更多信息，输入 `Get-Help Get-Credential`。

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
指定农场的行为（即农场在运行过程中的各种操作或策略）。

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
指定由 Active Directory Federation Services (AD FS) 服务使用的组托管服务帐户（Group Managed Service Account）的名称，该账户将作为 AD FS 服务的登录身份。

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

### -PrimaryComputerName
用于指定联邦服务器群中的主联邦服务器的名称。该cmdlet会检查是否存在您所指定的那台主联邦服务器的联邦服务器群。

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
指定主计算机的端口。计算机将使用您指定的HTTP端口与主计算机连接，以同步配置设置。请为该参数指定值80；如果主计算机的HTTP端口不是80，则可以指定其他数值。如果您不指定此参数，cmdlet会自动使用默认端口值443。

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
指定一个基于用户名和密码的 **PSCredential** 对象，该对象用于 Active Directory® Domain Services 中的服务账户（AD FS 服务即在该服务账户下运行）。要获取一个 **PSCredential** 对象，请使用 **Get-Credential** cmdlet。有关更多信息，请键入 `Get-Help Get-Credential`。

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
指定用于存储 AD FS 配置设置的 Microsoft SQL Server 数据库。如果您不指定此参数，AD FS 将使用 Windows 内部数据库来存储配置设置。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### System.Object

## 备注

## 相关链接

[Add-AdfsFarmNode](./Add-AdfsFarmNode.md)

[Test-AdfsFarmInstallation](./Test-AdfsFarmInstallation.md)

