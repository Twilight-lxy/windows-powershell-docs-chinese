---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: HgsServer-help.xml
Module Name: HgsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsserver/test-hgsserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-HgsServer
---

# 测试 HGS 服务器

## 摘要
测试本地计算机是否能够作为Host Guardian Service服务器节点运行。

## 语法

### PrimaryServer_HgsDomain（默认值）
```
Test-HgsServer [[-HgsDomainName] <String>] [-SafeModeAdministratorPassword <SecureString>]
 [-LogDirectory <String>] [-DatabasePath <String>] [<CommonParameters>]
```

### AdditionalServer
```
Test-HgsServer [[-HgsDomainName] <String>] [-HgsDomainCredential] <PSCredential> [-HgsServerIPAddress] <String>
 [-SafeModeAdministratorPassword <SecureString>] [-LogDirectory <String>] [-DatabasePath <String>]
 [<CommonParameters>]
```

## 描述
`Test-HgsServer` cmdlet 可以获取有关本地计算机的功能、配置和状态的信息，并将其与推荐设置进行比较，以确定该计算机是否可以作为 Host Guardian Service (HGS) 服务器节点正常运行。

在适用的情况下，会执行以下检查：

- HostGuardianServiceRole installation integrity
- BitLocker is enabled on the operating system drive
- SecureBoot is enabled
- Static IP addresses are configured
- Whether a restart is pending
- Prerequisites for installing a new forest or domain controller in Active Directory, this includes a test report
- Active Directory trust settings
- Validation tests for failover cluster hardware and settings
- Attestation application pool state
- Key Protection application pool state

有关场景术语的更多信息，请参阅[安全与保障](https://go.microsoft.com/fwlink/?LinkId=699209)。

## 示例

### 示例 1：测试第一个 HGS 节点
```
PS C:\> Test-HgsServer -HgsDomainName "Contoso.private"
```

此命令用于测试本地计算机是否可以充当第一个HGS节点。

### 示例 2：测试另一个 HGS 节点
```
PS C:\> $Cred = Get-Credential
PS C:\> Test-HgsServer -HgsDomainName "Contoso.private" -HgsServerIPAddress "100.100.100.1" -HgsDomainCredential $Cred
```

此命令用于测试本地计算机是否可以作为额外的 HGS 节点使用。

## 参数

### -DatabasePath
指定一个数据库路径。

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

### -HgsDomainCredential
指定用于主HGS服务器的Active Directory域管理员凭据。

```yaml
Type: PSCredential
Parameter Sets: AdditionalServer
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HgsDomainName
指定用于 HGS 服务器的 Active Directory 域的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HgsServerIPAddress
指定 HGS 服务器的网络 IP 地址。

```yaml
Type: String
Parameter Sets: AdditionalServer
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LogDirectory
指定输出日志文件的目录。

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

### -SafeModeAdministratorPassword
当计算机在安全模式（或安全模式的变体，例如目录服务恢复模式）下启动时，该设置用于指定管理员账户的密码。

```yaml
Type: SecureString
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

## 输出

### Microsoft.Windows.HostGuardianService.PowerShell.TestReport

## 备注

## 相关链接

[HGS 服务器 cmdlet](./hgsserver.md)

