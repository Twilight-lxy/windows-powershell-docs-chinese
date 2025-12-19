---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/get-wmssystem?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WmsSystem
---

# Get-WmsSystem

## 摘要
获取多点服务器（MultiPoint Server）的系统信息。

## 语法

```
Get-WmsSystem [-Server <String>] [<CommonParameters>]
```

## 描述
**Get-WmsSystem** cmdlet 可以获取 Windows MultiPoint Server 的系统信息。

## 示例

### 示例 1：获取系统信息
```
PS C:\> Get-WmsSystem
AttemptingToConnect        : False
RetryAttemptToConnect      : False
ProtocolVersion            : 1
WmsServerVersion           : 10.0.10586.0
WmsClientVersion           : 10.0.10586.0
NetJoinStatus              : NetSetupDomainName
DomainOrWorkgroupName      : TestDomain
SystemMode                 : Normal
DiskProtectionMode         : NotInstalled
ConnectionString           :
ConnectionCount            : 1
LicenseCount               : 0
State                      : Connected
ConnectionError            : 0
ConnectionErrorMessage     :
ComputerName               : Test1
WindowsEdition             : Windows Server 2016 Standard
IsVirtualMachine           : False
ManagedSystemsType         : MultiPointServers
MonitoringSystemType       : Include
IsSingleSessionPerUser     : True
MultiPointServers          : {}
PersonalComputers          : {}
CloudServers               : {}
ExcludedMultiPointServers  : {}
ExcludedPersonalComputers  : {}
ExcludedCloudServers       : {}
IPAddresses                :
ManagedServers             :
ExcludedManagedServers     : {}
IsSQMOn                    : True
IsWatsonOn                 : True
IsIPPerSessionEnabled      : False
IsChatEnabled              : True
HasNonLoopbackAdapter      : True
IsDesktopMonitoringAllowed : True
IsWmsSvcRunning            : True
IsScheduledUpdateEnabled      : False
ScheduleUpdateRunWU           : False
ScheduleUpdateCustomScript    :
MaxTimeAllowedForCustomScript : 0
ScheduledUpdatesReturnState   : __SUR_FIRST
TimeToScheduleUpdates         : 0
IsAllowRemoteManagementOn     : True
BootToConsoleMode             : False
SuppressPrivacyNotification   : False
SystemImage                   :
```

该命令用于获取MultiPoint Server的系统信息。

## 参数

### -Server
指定该命令的目标（即MultiPoint Server）的完整主机名。默认值为localhost。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ComputerName

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### Microsoft.WindowsServerSolutions.MultipointServer.PowerShell Commands.Library.WmsSystem

## 备注

## 相关链接

[Add-WmsSystem](./Add-WmsSystem.md)

[Remove-WmsSystem](./Remove-WmsSystem.md)

[重启 WMS 系统](./Restart-WmsSystem.md)

[Search-WmsSystem](./Search-WmsSystem.md)

[Set-WmsSystem](./Set-WmsSystem.md)

[Stop-WmsSystem](./Stop-WmsSystem.md)

