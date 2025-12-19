---
description: 从指定的 Active Directory（AD）计算机或域控制器对象中查询 Windows 本地管理员密码解决方案（LAPS）的凭据。
external help file: lapspsh.dll-Help.xml
Module Name: LAPS
online version: https://learn.microsoft.com/powershell/module/laps/get-lapsadpassword?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
Locale: en-US
ms.date: 04/10/2023
title: Get-LapsADPassword
---

# 获取 Get-LapsADPassword 的密码

## 摘要
从指定的 Active Directory（AD）计算机或域控制器对象中查询 Windows 本地管理员密码解决方案（LAPS）的凭据。

## 语法

### NormalMode（默认值）

```
Get-LapsADPassword [-Credential <PSCredential>] [-DecryptionCredential <PSCredential>]
 [-IncludeHistory] [-AsPlainText] [-Identity] <String[]> [<CommonParameters>]
```

### DomainMode

```
Get-LapsADPassword [-Credential <PSCredential>] [-DecryptionCredential <PSCredential>]
 [-IncludeHistory] [-AsPlainText] [-Identity] <String[]> -Domain <String> [<CommonParameters>]
```

### DomainControllerMode

```
Get-LapsADPassword [-Credential <PSCredential>] [-DecryptionCredential <PSCredential>]
 [-IncludeHistory] [-AsPlainText] [-Identity] <String[]> -DomainController <String>
 [<CommonParameters>]
```

### SnapshotBrowserMode

```
Get-LapsADPassword [-Credential <PSCredential>] [-DecryptionCredential <PSCredential>]
 [-IncludeHistory] [-AsPlainText] -Port <Int32> [-Identity] <String[]> [-DomainController <String>]
 [<CommonParameters>]
```

### RecoveryMode

```
Get-LapsADPassword [-IncludeHistory] [-AsPlainText] [-RecoveryMode] [-Identity] <String[]>
 [<CommonParameters>]
```

### SnapshotBrowserRecoveryMode

```
Get-LapsADPassword [-IncludeHistory] [-AsPlainText] [-RecoveryMode] -Port <Int32>
 [-Identity] <String[]> [<CommonParameters>]
```

## 描述

`Get-LapsADPassword` cmdlet 允许管理员获取 Active Directory 计算机或域控制器对象的密码以及密码历史记录。根据策略配置的不同，LAPS 密码可能以明文形式或加密形式存储。`Get-LapsADPassword` cmdlet 会自动解密加密后的密码。

`Get-LapsADPassword` cmdlet 也可以用于连接到已挂载的 Active Directory (AD) 快照。

`Verbose` 参数可用于获取有关该 cmdlet 操作的更多信息。

## 示例

### 示例 1

```powershell
Get-LapsADPassword LAPSCLIENT
```

```Output
ComputerName        : LAPSCLIENT
DistinguishedName   : CN=LAPSCLIENT,OU=LapsTestOU,DC=laps,DC=com
Account             : Administrator
Password            : System.Security.SecureString
PasswordUpdateTime  : 4/9/2023 10:03:41 AM
ExpirationTimestamp : 4/14/2023 10:03:41 AM
Source              : CleartextPassword
DecryptionStatus    : NotApplicable
AuthorizedDecryptor : NotApplicable
```

这个示例演示了如何查询当前域中 `LAPSCLIENT` 计算机的当前 LAPS 密码。该密码以明文形式存储在 Active Directory (AD) 中，因此无需解密。返回的密码被封装在一个 **SecureString** 对象中。

### 示例 2

```powershell
Get-LapsADPassword -Identity LAPSCLIENT -DomainController lapsDC -AsPlainText
```

```Output
ComputerName        : LAPSCLIENT
DistinguishedName   : CN=LAPSCLIENT,OU=LapsTestOU,DC=laps,DC=com
Account             : Administrator
Password            : k8P]Xl5T-ky!aj4s21el3S#.x44!e{8+,{L!M
PasswordUpdateTime  : 4/9/2023 10:03:41 AM
ExpirationTimestamp : 4/14/2023 10:03:41 AM
Source              : CleartextPassword
DecryptionStatus    : NotApplicable
AuthorizedDecryptor : NotApplicable
```

这个示例演示了如何在特定的域控制器（`lapsDC`）上查询与`LAPSCLIENT`计算机相关的当前LAPS密码，并要求以明文形式显示该密码。该密码是以明文形式存储在Active Directory（AD）中的，因此无需解密；最终返回的密码也是以明文形式提供的。

### 示例 3

```powershell
Get-LapsADPassword -Identity LAPSCLIENT2 -Domain laps.com -AsPlainText -IncludeHistory
```

```Output
ComputerName        : LAPSCLIENT2
DistinguishedName   : CN=LAPSCLIENT2,OU=LapsTestEncryptedOU,DC=laps,DC=com
Account             : Administrator
Password            : q64!7KI3BOe/&S%buM0nBaW{B]261zN5L0{;{
PasswordUpdateTime  : 4/9/2023 9:39:38 AM
ExpirationTimestamp : 4/14/2023 9:39:38 AM
Source              : EncryptedPassword
DecryptionStatus    : Success
AuthorizedDecryptor : LAPS\LAPS Admins

ComputerName        : LAPSCLIENT2
DistinguishedName   : CN=LAPSCLIENT2,OU=LapsTestEncryptedOU,DC=laps,DC=com
Account             : Administrator
Password            : O{P61q6bu(3kZ6&#p2y.&F$cWd;0dm8!]Wl5j
PasswordUpdateTime  : 4/9/2023 9:38:10 AM
ExpirationTimestamp :
Source              : EncryptedPasswordHistory
DecryptionStatus    : Success
AuthorizedDecryptor : LAPS\LAPS Admins
```

这个示例演示了如何在特定的 Active Directory（AD）域（`laps.com`）中查询 `LAPSCLIENT2` 计算机的当前 LAPS 密码，并要求以明文形式显示该密码。该密码在 AD 中是以加密形式存储的，最终成功解密了。

> [注意] > 对于任何返回的旧版LAPS密码，`ExpirationTimestamp`字段始终为空。

### 示例 4

```powershell
Get-LapsADPassword -Identity lapsDC.laps.com -AsPlainText
```

```Output
ComputerName        : LAPSDC
DistinguishedName   : CN=LAPSDC,OU=Domain Controllers,DC=laps,DC=com
Account             : Administrator
Password            : 118y$rsw.3y58yG]on$Hii
PasswordUpdateTime  : 4/9/2023 10:17:51 AM
ExpirationTimestamp : 4/19/2023 10:17:51 AM
Source              : EncryptedDSRMPassword
DecryptionStatus    : Success
AuthorizedDecryptor : LAPS\Domain Admins
```

这个示例展示了如何查询 `lapsDC.laps.com` 域控制器的当前密码，并要求以明文形式显示该密码。该密码原本以加密形式存储在 Active Directory (AD) 中，但最终成功被解密了。

### 示例 5

```powershell
Get-LapsADPassword LAPSDC
```

```Output
ComputerName        : LAPSDC
DistinguishedName   : CN=LAPSDC,OU=Domain Controllers,DC=laps,DC=com
Account             :
Password            :
PasswordUpdateTime  : 4/9/2023 10:17:51 AM
ExpirationTimestamp : 4/19/2023 10:17:51 AM
Source              : EncryptedDSRMPassword
DecryptionStatus    : Unauthorized
AuthorizedDecryptor : LAPS\Domain Admins
```

这个示例展示了在用户没有权限解密 LAPS DSRM 密码的情况下，如何查询 `LAPSDC` 域控制器的当前 LAPS 密码。

### 示例 6

```powershell
Get-LapsADPassword LAPSLEGACYCLIENT -AsPlainText
```

```Output
ComputerName        : LAPSLEGACYCLIENT
DistinguishedName   : CN=LAPSLEGACYCLIENT,OU=LegacyLapsOU,DC=laps,DC=com
Account             :
Password            : Z#x}&7BluHf3{r+C218
PasswordUpdateTime  :
ExpirationTimestamp : 5/14/2023 1:55:39 PM
Source              : LegacyLapsCleartextPassword
DecryptionStatus    : NotApplicable
AuthorizedDecryptor : NotApplicable
```

这个示例演示了如何查询当前处于传统LAPS仿真模式下的‘LAPSLEGACYCLIENT’机器的LAPS密码。

> [!注意] > 在查询旧式的LAPS风格密码时，**Account**（账户）和**PasswordUpdateTime**（密码更新时间）字段始终是不可用的。

### 示例 7

```powershell
Get-LapsADPassword -Identity LAPSCLIENT -Port 50000 -AsPlainText
```

```Output
ComputerName        : LAPSCLIENT
DistinguishedName   : CN=LAPSCLIENT,OU=LapsTestOU,DC=laps,DC=com
Account             : Administrator
Password            : H6UycL[vj#zzTNVpS//G2{j&t9aO}k[K5l4)X
PasswordUpdateTime  : 4/15/2023 6:51:45 AM
ExpirationTimestamp : 4/20/2023 6:51:45 AM
Source              : CleartextPassword
DecryptionStatus    : NotApplicable
AuthorizedDecryptor : NotApplicable
```

这个示例展示了如何查询 AD 断面浏览器实例，以获取 `LAPSCLIENT` 机器当前的 LAPS 密码。该示例假设断面浏览器已经在本地机器上启动，并监听着 `50000` 端口的 LDAP 请求。

## 参数

### -AsPlainText

请指定此参数，以便以明文格式返回 LAPS 密码。默认情况下，LAPS 密码会封装在一个.NET的**SecureString**对象中返回。

> [!重要!] > 使用此参数会导致返回的明文密码被随意查看，从而可能带来安全风险。应谨慎使用该参数，并且仅限于支持或测试场景。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential

指定一组凭据，用于在查询 Active Directory（AD）以获取 LAPS 凭据时使用。如果未指定，则会使用当前用户的凭据。

```yaml
Type: System.Management.Automation.PSCredential
Parameter Sets: NormalMode, DomainMode, DomainControllerMode, SnapshotBrowserMode
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DecryptionCredential

指定一组用于解密加密后的LAPS凭据的凭据信息。如果未指定，则使用当前用户的凭据。

```yaml
Type: System.Management.Automation.PSCredential
Parameter Sets: NormalMode, DomainMode, DomainControllerMode, SnapshotBrowserMode
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Domain

指定要连接的域的名称。

```yaml
Type: System.String
Parameter Sets: DomainMode
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DomainController

指定要连接的域控制器的名称，或者运行 AD Snapshot Browser 的远程服务器的名称。

```yaml
Type: System.String
Parameter Sets: DomainControllerMode
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: System.String
Parameter Sets: SnapshotBrowserMode
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity

指定要从其中检索 LAPS 凭据的计算机或域控制器对象的名称。

此参数支持多种不同的名称格式，这些格式会影响在 Active Directory（AD）中搜索目标设备时所使用的标准。支持的名称格式如下：

- distinguishedName (begins with a `CN=`)
- samAccountName (begins with a '$")
- dnsHostName (contains at least one '.' character)
- name (for all other inputs)

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -IncludeHistory

指定计算机对象上任何较旧的LAPS凭据也应当被显示出来。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Port

指定要连接的 AD 快照浏览器端口。

```yaml
Type: System.Nullable`1[System.Int32]
Parameter Sets: SnapshotBrowserMode, SnapshotBrowserRecoveryMode
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RecoveryMode

当无法通过常规机制解密给定的 LAPS 凭据时，此参数提供了一个最后的解决方案。例如，如果某个 LAPS 凭据是使用一个已被删除的组进行加密的，那么就可能需要使用这个方法来解密该凭证。

> [!重要提示] > 在指定此参数时，您必须以域管理员的身份在本地登录到可写入的域控制器上。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: RecoveryMode, SnapshotBrowserRecoveryMode
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

## 输出

### System.Object

## 备注

## 相关链接

[Windows LAPS概述](https://go.microsoft.com/fwlink/?linkid=2233901)

[开始使用 Windows LAPS 和 Windows Server Active Directory](https://go.microsoft.com/fwlink/?linkid=2233705)
